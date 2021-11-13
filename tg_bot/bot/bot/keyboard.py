from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice_bt = InlineKeyboardMarkup(row_width=1)
b_t = InlineKeyboardButton(text="Выбрать командировку", callback_data='choice_bt')
choice_bt.insert(b_t)
