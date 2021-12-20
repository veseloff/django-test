"""Обработчик сообщений"""
from scaner import read_qr
from tg_bot.bot.bot.loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from tg_bot.bot.bot.nalog_python import NalogRuPython
from tg_bot.bot.bot.parse_fns_answer import parser_fns
from db_comands import DBCommands
from keyboard import choice_bt, yes_no, close_bt, yes_close,\
    change_phone, close_all
from state import Scanner
import re
import os


db = DBCommands()


@dp.callback_query_handler(text_contains='get_id')
async def get_id(call: CallbackQuery):
    """
    Получение id пользователя в telegram
    Args:
        call:

    Returns:

    """
    await call.answer(cache_time=60)
    user_id = call.from_user.id
    await call.message.answer(f'Ваш id: {user_id}')


@dp.callback_query_handler(text_contains="choice_bt", state=None)
async def choose_business_trip(call: CallbackQuery, state: FSMContext):
    """
    Уточнение командировки
    Args:
        call:
        state:

    Returns:

    """
    await call.answer(cache_time=60)
    await Scanner.ChooseBusinessTrip.set()
    user_id_telegram = call.from_user.id
    user_id_system = await db.find_user_id(user_id_telegram)
    await state.update_data(user_id_system=user_id_system)
    business_trip = await db.find_business_trip(user_id_system)
    if business_trip is not None:
        await call.message.answer(f'Добавить чек к: {business_trip["name"]}?', reply_markup=yes_no)
        await state.update_data(b_t_id=business_trip['id'])
    else:
        await call.message.answer(f'У вас нет действующей командировки, '
                                  f'вы можете добавить чек к уже законченной последней командировке '
                                  f'или проверить статус вашей командировки на нашем сайте и повторить',
                                  reply_markup=close_bt)


@dp.callback_query_handler(text_contains="yes", state=Scanner.ChooseBusinessTrip)
async def choose_number_phone(call: CallbackQuery, state: FSMContext):
    """
    Проверка номера телефона и отправка кода для регистрации на фнс
    Args:
        call:
        state:

    Returns:

    """
    await call.answer(cache_time=60)
    data = await state.get_data()
    phone = data.get("phone")
    if phone is None:
        phone = await db.find_phone(call.from_user.id)
        if len(phone) == 0:
            await Scanner.InsertPhone.set()
            return await call.message.answer('Кажется, у нас нет вашего номера телефона,'
                                             ' пожалуйста введите его в формате +7ХХХХХХХХХХ,'
                                             'это нужно для подтверждения смс-кода', reply_markup=close_all)
        else:
            if re.fullmatch(r'89\d{9}', phone):
                phone = '7' + phone[1:]
            phone = f'+{phone}'
            await state.update_data(phone=phone)
    if re.fullmatch(r'\+79\d{9}', phone) is None:
        await Scanner.InsertPhone.set()
        return await call.message.answer('Ваше телефон введёт неверно, введите его в формате +7ХХХХХХХХХХ',
                                         reply_markup=close_all)
    client = NalogRuPython(phone)
    await state.update_data(client=client)
    await Scanner.CodeConfirmation.set()
    await call.message.answer(f'На ваш номер телефона {phone} сейчас придёт код с смс подтверждением, '
                              'отправьте его нам.'
                              'Введите код без пробелов и прочих символов.', reply_markup=change_phone)


@dp.callback_query_handler(text_contains="no", state=Scanner.ChooseBusinessTrip)
async def find_close_bt(call: CallbackQuery, state: FSMContext):
    """
    Найти последнюю законченную командировку
    Args:
        call:
        state:

    Returns:

    """
    await call.answer(cache_time=60)
    data = await state.get_data()
    user_id_system = data['user_id_system']
    b_t = await db.find_close_business_trip(user_id_system)
    if len(b_t) > 0:
        last_b_t = b_t[-1]
        await call.message.answer(f'Добавить чек к {last_b_t["name"]}?', reply_markup=yes_close)
        await state.update_data(b_t_id=last_b_t['id'])
    else:
        await call.message.answer('У вас нет законченных командировок', reply_markup=close_all)
        await state.finish()


@dp.message_handler(state=Scanner.CodeConfirmation)
async def code_confirmation(message: Message, state: FSMContext):
    """
    Подтверждение смс кода с сайта фнс
    Args:
        message:
        state:

    Returns:

    """
    code = message.text.split(' ')
    data = await state.get_data()
    client = data['client']
    status = client.code_confirmation(code)
    if status == 200:
        await state.update_data(client=client)
        await Scanner.AddCheque.set()
        await message.answer(f'Отправьте фото чека.\n'
                             f'Дождитесь сообщения об успешной обработке чека, '
                             f'перед следущей отправкой.')
    else:
        await message.answer('Вы ввели неверный код, или ввели лишний символ попробуйте ещё раз',
                             reply_markup=close_all)


@dp.message_handler(content_types=['document', 'photo'], state=Scanner)
async def handle_docs_photo(message: Message, state: FSMContext):
    """
    Получаем и обрабатываем чек
    Args:
        message:
        state:

    Returns:

    """
    data = await state.get_data()
    id_b_t = data['b_t_id']
    filename = f'{id_b_t}.png'
    if message.document is None:
        await message.photo[-1].download(filename)
    else:
        await message.document.download(filename)
    qr_code = read_qr(filename)
    os.remove(filename)
    client = data['client']
    ticket = client.get_ticket(qr_code)
    date_answer, items, check_amount, date_db = parser_fns(ticket)
    report_for_db = ''
    for item in items:
        report_for_db += f'{item}\n'
    report = f'Дата покупки: {date_answer}\n' + report_for_db + f'Сумма покупки {check_amount}'
    await message.answer(report, reply_markup=close_all)

    arg_to_db = (check_amount, date_db, report_for_db, id_b_t)
    await db.add_new_cheque(arg_to_db)
    await message.answer('Чек успешно добавлен.', reply_markup=close_all)


@dp.message_handler(state=Scanner.InsertPhone)
async def insert_phone(message: Message, state: FSMContext):
    """
    Добавить номер телефона
    Args:
        message:
        state:

    Returns:

    """
    phone = message.text
    if re.fullmatch(r'\+79\d{9}', phone):
        params = (phone[1:], message.from_user.id)
        await db.update_phone(params)
        await state.update_data(phone=phone)
        client = NalogRuPython(phone)
        await state.update_data(client=client)
        await Scanner.CodeConfirmation.set()
        await message.answer(f'На ваш номер телефона {phone} сейчас придёт код с смс подтверждением, '
                             'отправьте его нам.'
                             'Введите код без пробелов и прочих символов.', reply_markup=close_all)
    else:
        await message.answer('Не корректный номер телефона', reply_markup=close_all)


@dp.callback_query_handler(text_contains='change_phone', state=Scanner.CodeConfirmation)
async def update_phone(call: CallbackQuery):
    """
    Изменить номер телефона
    Args:
        call:

    Returns:

    """
    await call.answer(cache_time=60)
    await Scanner.InsertPhone.set()
    return await call.message.answer('Введите номер телефона в формате +7ХХХХХХХХХХ,'
                                     'это нужно для подтверждения смс-кода', reply_markup=close_all)


@dp.callback_query_handler(text_contains="close", state=Scanner)
async def close(call: CallbackQuery, state: FSMContext):
    """
    Выйти из всех состояний
    Args:
        call:
        state:

    Returns:

    """
    await call.answer(cache_time=60)
    await call.message.answer('Чтобы начать сначала, напишите что угодно или нажмите /start')
    await state.finish()


@dp.message_handler()
async def choose_action(message: Message):
    """
    Начало общения
    Args:
        message:

    Returns:

    """
    await message.answer('Выберите действие', reply_markup=choice_bt)
