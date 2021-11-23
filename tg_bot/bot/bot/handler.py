from scaner import get_info_zxing_qrscanner
from tg_bot.bot.bot.loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from tg_bot.bot.bot.nalog_python import NalogRuPython
from tg_bot.bot.bot.fnl_requests import json_parser
from db_comands import DBCommands
from datetime import datetime
from keyboard import choice_bt, yes_no, close_bt, yes_close
from state import Scanner


db = DBCommands()


@dp.message_handler(commands=['start'])
async def get_id(message: Message):
    """
    Получение id пользователя в telegram при первом запуске или команде start
    Args:
        message:
        state:

    Returns:

    """
    user_id = message.from_user.id
    await message.answer(f'Ваш id: {user_id}')


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
    Уточнение командировки
    Args:
        call:
        state:

    Returns:

    """
    await call.answer(cache_time=60)
    data = await state.get_data()
    phone = data.get("phone")
    if phone is None:
        phone = db.find_phone(call.from_user.id)
        if phone is None:
            await Scanner.InsertPhone.set()
            return await call.message.answer('Кажется у нас нет вашего номера телефона,'
                                             ' пожалуйста введите его в формате +7ХХХХХХХХХХ,'
                                             'это нужно для подтверждения смс-кода')
        else:
            await state.update_data(phone=phone)
    await Scanner.AddCheque.set()
    return await call.message.answer(f'Отправьте фото чека.\n'
                                     f'Дождитесь сообщения об успешной обработке чека, '
                                     f'перед следущей отправкой.')


@dp.callback_query_handler(text_contains="no", state=Scanner.ChooseBusinessTrip)
async def find_close_bt(call: CallbackQuery, state: FSMContext):
    """
    Уточнение командировки
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
        await call.message.answer('У вас нет законченных командировок')
        await state.finish()


@dp.message_handler(content_types=['document', 'photo'], state=Scanner.AddCheque)
async def handle_docs_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    id_b_t = data['b_t_id']
    if message.document is None:
        await message.photo[-1].download(f'{id_b_t}')
    else:
        await message.document.download(f'{id_b_t}')
    filename = str(id_b_t)

    client = NalogRuPython()
    qr_code = get_info_zxing_qrscanner(filename)
    ticket = client.get_ticket(qr_code)
    data_cheque = json_parser(ticket)

    arg = (data_cheque[2], datetime.now(), "Сыр 3", 1)
    await db.add_new_cheque(arg)
    result_answer = ""
    for el in data_cheque[1]:
        result_answer = result_answer + '\n' + el
    report = f"{data_cheque[0]} Вы купили: {result_answer}  \n \n Потратив всего: {data_cheque[2]} \u20bd"
    await message.answer(report)
    report = "Обед 111"
    b_t_data = await state.get_data()
    b_t_id = b_t_data.get('b_t_id')
    params_to_insert = (111, datetime.now(), report, b_t_id)
    await db.add_new_cheque(params_to_insert)
    await message.answer('Чек успешно добавлен, мо')


@dp.callback_query_handler(text_contains="close", state=Scanner)
async def close(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.answer('Чтобы начать сначала, напишите что угодно')
    await state.finish()


@dp.message_handler()
async def choose_action(message: Message):
    await message.answer('Выберите действие', reply_markup=choice_bt)

