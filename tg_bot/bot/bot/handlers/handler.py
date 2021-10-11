from tg_bot.bot.bot.loader import dp, bot
import logging
from tg_bot.bot.bot.loader import dp, bot
from aiogram.types import Message, CallbackQuery, PhotoSize, File
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
#from PIL import Image


# @dp.message_handler()
# async def exo(message: Message):
#     await message.answer(f'Ты написал {message.text}.\n Я жду команду /start')

# @dp.message_handler(content_types=["photo"])
# def echo_msg(message):
#     if message.content_type == 'photo':
#         raw = message.photo[2].file_id
#         name = raw + ".jpg"
#         file_info = dp.get_file(raw)
#         downloaded_file = dp.download_file(file_info.file_path)
#         with open(name, 'wb') as new_file:
#             new_file.write(downloaded_file)
#         img = open(name, 'rb')
#         # bot.send_message(chatID, "Запрос от\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name), parse_mode="Markdown") #от кого идет сообщение и его содержание
#         # bot.send_photo(chatID, img)
#         # bot.send_message(message.chat.id, "*{name}!*\n\nСпасибо за инфу".format(name=message.chat.first_name, last=message.chat.last_name, text=message.text), parse_mode="Markdown") #то что пойдет юзеру после отправки сообщения


@dp.message_handler(content_types=['document', 'photo'])
async def handle_docs_photo(message: Message):
    print("Зашел")
    print(type(message.photo))
    print(message.photo[0])
    print('поймал фото')
    # try:
    #
    #     file_info = dp.get_file(message.document.file_id)
    #     downloaded_file = dp.download_file(file_info.file_path)
    #
    #     src = 'C:/Python/Project/tg_bot/files/received/' + message.document.file_name;
    #     with open(src, 'wb') as new_file:
    #          new_file.write(downloaded_file)
    #     message.imgbars = (Image.open(arg_image_path), symbols=[ZBarSymbol.QRCODE])
    #     dp.reply_to(message, "Пожалуй, я сохраню это")
    #     await message.answer('Test')
    #
    # except Exception as e:
    #     await message.answer('Test failed')


@dp.message_handler()
async def exo(message: Message):
    await message.answer(f'Ты написал {message.text}.\n Я жду команду /start')

    #
    #

    #
    #
    #
    #
    # # @dp.message_handler(content_types=["photo"])
    # # def echo_msg(message):
    # #     if message.content_type == 'photo':
    # #         raw = message.photo[2].file_id
    # #         name = raw + ".jpg"
    # #         file_info = dp.get_file(raw)
    # #         downloaded_file = dp.download_file(file_info.file_path)
    # #         with open(name, 'wb') as new_file:
    # #             new_file.write(downloaded_file)
    # #         img = open(name, 'rb')
    # #         # bot.send_message(chatID, "Запрос от\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name), parse_mode="Markdown") #от кого идет сообщение и его содержание
    # #         # bot.send_photo(chatID, img)
    # #         # bot.send_message(message.chat.id, "*{name}!*\n\nСпасибо за инфу".format(name=message.chat.first_name, last=message.chat.last_name, text=message.text), parse_mode="Markdown") #то что пойдет юзеру после отправки сообщения