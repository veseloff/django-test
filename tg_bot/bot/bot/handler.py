from scaner import get_info_zxing_qrscanner
from tg_bot.bot.bot.loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from tg_bot.bot.bot.nalog_python import NalogRuPython
from tg_bot.bot.bot.fnl_requests import json_parser
from db_comands import DBCommands
from datetime import datetime
from keyboard import choice_bt, yes_no
from state import Scanner


db = DBCommands()


@dp.message_handler(commands=['start'])
async def get_id(message: Message, state: FSMContext):
    """
    Получение id пользователя в telegram
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
    user_id_telegram = call.from_user.id
    user_id_system = await db.find_user_id(user_id_telegram)
    params = ('79122165385', user_id_telegram)
    await db.update_phone(params)
    await Scanner.ChoosePhone.set()
    business_trip = await db.find_business_trip(user_id_system)
    await call.message.answer(f'Текущая командировка: {business_trip["name"]}', reply_markup=yes_no)
    await state.update_data(b_t_id=business_trip['id'])



@dp.callback_query_handler(text_contains="yes", state=Scanner.ChoosePhone)
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
        if phone == '': #?????
            await Scanner.InsertPhone.set()
            return await call.message.answer('Кажется у нас нет вашего номера телефона,'
                                             ' пожалуйста введите его в формате +7ХХХХХХХХХХ')
        else:
            await state.update_data(phone=phone)
    return await call.message.answer(f'Отправьте фото чека')


@dp.message_handler(content_types=['document', 'photo'], state=Scanner.ChooseBusinessTrip)
async def handle_docs_photo(message: Message, state: FSMContext):
    # if message.document is None:
    #     await message.photo[-1].download('чек1.jpg')
    #     filename = 'чек1.jpg'
    # else:
    #     await message.document.download('чек2.jpg')
    #     filename = 'чек2.jpg'
    # client = NalogRuPython()
    # qr_code = get_info_zxing_qrscanner(filename)
    # ticket = client.get_ticket(qr_code)
    # data_checka = json_parser(ticket)
    # arg = (data_checka[2], datetime.now(), "Сыр 3", 1)
    # await db.add_new_cheque(arg)
    # result_answer = ""
    # for el in data_checka[1]:
    #     result_answer = result_answer + '\n' + el
    # report = f"{data_checka[0]} Вы купили: {result_answer}  \n \n Потратив всего: {data_checka[2]} \u20bd"
    # await message.answer(report)
    report = "Обед 111"
    b_t_data = await state.get_data()
    b_t_id = b_t_data.get('b_t_id')
    params_to_insert = (111, datetime.now(), report, b_t_id)
    await db.add_new_cheque(params_to_insert)
    await message.answer('Чек успешно добавлен')


@dp.message_handler()
async def choose_action(message: Message):
    await message.answer('Выберите действие', reply_markup=choice_bt)

