from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice_bt = InlineKeyboardMarkup(row_width=1)
b_t = InlineKeyboardButton(text="Выбрать командировку", callback_data='choice_bt')
choice_bt.insert(b_t)

yes_no = InlineKeyboardMarkup(row_width=2)
yes = InlineKeyboardButton(text="Да", callback_data='yes')
no = InlineKeyboardButton(text="Нет", callback_data='no')
yes_no.insert(yes)
yes_no.insert(no)
