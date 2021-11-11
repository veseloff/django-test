from loader import db


class DBCommands:
    pool = db
    ADD_NEW_CHEQUE = "INSERT INTO user_profile_cheque (amount, date_time, report, business_trip_id) " \
                     "VALUES (%s, %s, %s, %s)"

    ADD_NEW_USER = "INSERT INTO user_profile_uesr_telegram (id_telegram, user_id, tag) " \
                   "VALUES (%s, %s, %s, %s)"

    async def add_new_cheque(self, args):
        command = self.ADD_NEW_CHEQUE
        await self.pool.fetchval(command, args)

    async def add_new_user(self, args):
        command = self.ADD_NEW_USER
        await self.pool.fetchval(command, args)
