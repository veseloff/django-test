from aiogram.dispatcher.filters.state import StatesGroup, State


class Scanner(StatesGroup):
    ChooseBusinessTrip = State()
    SendScanner = State()