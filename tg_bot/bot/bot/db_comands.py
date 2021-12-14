"""Модуль взаимодействия с базой данных"""
from loader import db
from datetime import date


class DBCommands:
    pool = db
    ADD_NEW_CHEQUE = "INSERT INTO user_profile_cheque (amount, date_time, report, business_trip_id) " \
                     "VALUES ($1, $2, $3, $4)"

    FIND_BUSINESS_TRIP = f"SELECT * FROM user_profile_businesstrip WHERE date_start <= $2 " \
                         f"AND $2 <= date_finish AND user_id=$1"

    FIND_CLOSE_BUSINESS_TRIP = f"SELECT * FROM user_profile_businesstrip WHERE $2 > date_finish " \
                               f"AND user_id=$1"

    FIND_USER_ID_IN_SYSTEM = "SELECT user_id FROM user_profile_usertelegram WHERE id_telegram=$1"

    FIND_TELEPHONE = "SELECT telephone FROM user_profile_usertelegram WHERE id_telegram=$1"

    UPDATE_TELEPHONE = "UPDATE user_profile_usertelegram SET telephone=$1 WHERE id_telegram=$2"

    async def add_new_cheque(self, args):
        """
        Добавление чека
        Args:
            args:

        Returns:

        """
        command = self.ADD_NEW_CHEQUE
        return await self.pool.fetchval(command, *args)

    async def find_business_trip(self, user_id):
        """
        Нахождение командировки
        Args:
            user_id:

        Returns:

        """
        command = self.FIND_BUSINESS_TRIP
        return await self.pool.fetchrow(command, user_id, date.today())

    async def find_user_id(self, telegram_id):
        """
        Найти id пользователя в систему по id телеграме
        Args:
            telegram_id:

        Returns:

        """
        command = self.FIND_USER_ID_IN_SYSTEM
        return await self.pool.fetchval(command, telegram_id)

    async def find_phone(self, telegram_id):
        """
        Найти телефон пользователя
        Args:
            telegram_id:

        Returns:

        """
        command = self.FIND_TELEPHONE
        return await self.pool.fetchval(command, telegram_id)

    async def update_phone(self, args):
        """
        Обновить телефон пользователя
        Args:
            args:

        Returns:

        """
        command = self.UPDATE_TELEPHONE
        return await self.pool.fetchval(command, *args)

    async def find_close_business_trip(self, user_id):
        """
        Найти законченные командировки
        Args:
            user_id:

        Returns:

        """
        command = self.FIND_CLOSE_BUSINESS_TRIP
        return await self.pool.fetch(command, user_id, date.today())
