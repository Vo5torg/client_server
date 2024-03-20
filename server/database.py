import aiosqlite
import asyncio


class AsyncDataBase:
    @staticmethod
    async def create_tables():
        try:
            async with aiosqlite.connect('database.db') as db:
                await db.execute('CREATE TABLE IF NOT EXISTS Users '
                                 '(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT UNIQUE NOT NULL, '
                                 'password TEXT NOT NULL, is_admin BOOL, ip_address TEXT );')
                await db.execute('CREATE TABLE IF NOT EXISTS Permissions '
                                 '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                                 'login text, bin BOOL, oct BOOL, dec BOOL, hex BOOL);')
                await db.execute('CREATE TABLE IF NOT EXISTS BlockedIP'
                                 '(id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT);')
                await db.commit()
                return True
        except Exception as Ex:
            return False

    @staticmethod
    async def add_user(login, password, admin, ip_address):
        try:
            async with aiosqlite.connect('database.db') as db:
                await db.execute('INSERT INTO Users (login, password, is_admin, ip_address) VALUES (?, ?, ?, ?);',
                                 (login, password, admin, ip_address))
                await db.execute(
                    'INSERT INTO Permissions (login, bin, oct, dec, hex) VALUES (?, ?, ?, ?, ?);',
                    (login, True, True, True, True))

                await db.commit()
                return True
        except Exception as Ex:
            return False

    @staticmethod
    async def delete_user(login):
        try:
            async with aiosqlite.connect('database.db') as db:
                await db.execute('DELETE FROM Users WHERE login = ? ;', (login,))
                await db.execute('DELETE FROM Permissions WHERE login = ? ;', (login,))
                await db.commit()
                return True
        except Exception as Ex:
            return False

    @staticmethod
    async def get_user(login):
        try:
            async with aiosqlite.connect('database.db') as db:
                cursor = await db.execute('SELECT * FROM Users WHERE login = ?;', (login,))
                rows = await cursor.fetchall()
                if rows:
                    return rows[0]
                return False
        except Exception as Ex:
            return False

    @staticmethod
    async def get_users():
        try:
            async with aiosqlite.connect('database.db') as db:
                cursor = await db.execute('SELECT * FROM Users;')
                rows = await cursor.fetchall()
                if rows:
                    return rows
                return False
        except Exception as Ex:
            return False

    @staticmethod
    async def get_permission(login):
        try:
            async with aiosqlite.connect('database.db') as db:
                cursor = await db.execute('SELECT * FROM Permissions WHERE login = ?;', (login,))
                rows = await cursor.fetchall()
                if rows:
                    return rows[0]
                return False
        except Exception as Ex:
            return False

    @staticmethod
    async def set_permission(login, option, value):
        try:
            async with aiosqlite.connect('database.db') as db:
                await db.execute(
                    'UPDATE Permissions SET "{}" = ? WHERE login = ? ;'.format(option.replace('"', '""')),
                    (value, login,))
                await db.commit()
                return True
        except Exception as Ex:
            return False

    @staticmethod
    async def show_block_ip():
        try:
            async with aiosqlite.connect('database.db') as db:
                cursor = await db.execute('SELECT * FROM BlockedIP;')
                rows = await cursor.fetchall()
                if rows:
                    return rows
                return False
        except Exception as Ex:
            return False

    @staticmethod
    async def block_ip(ip):
        try:
            async with aiosqlite.connect('database.db') as db:
                await db.execute('INSERT INTO BlockedIP (ip) VALUES (?);', (ip,))
                await db.commit()
                return True
        except Exception as Ex:
            return False

    @staticmethod
    async def allow_ip(ip):
        try:
            async with aiosqlite.connect('database.db') as db:
                await db.execute('DELETE FROM BlockedIP WHERE ip = ? ;', (ip,))
                await db.commit()
                return True
        except Exception as Ex:
            return False

    @staticmethod
    async def is_admin(login):
        try:
            async with aiosqlite.connect('database.db') as db:
                cursor = await db.execute('SELECT * FROM Users WHERE login = ?;', (login,))
                rows = await cursor.fetchall()
                if rows:
                    if rows[0][3]:
                        return True
                return False
        except Exception as Ex:
            return False

    @staticmethod
    async def is_ip_blocked(ip):
        try:
            async with aiosqlite.connect('database.db') as db:
                cursor = await db.execute('SELECT * FROM BlockedIP WHERE ip = ?;', (ip,))
                rows = await cursor.fetchall()
                if rows:
                    return True
                return False
        except Exception as Ex:
            return False


async def run():
    data_base = AsyncDataBase()
    await data_base.create_tables()
    await data_base.add_user("admin", "admin", "True", "192.168.0.1")
    # await data_base.delete_user("admin")
    # await data_base.block_ip("192.127.0.2")
    # await data_base.allow_ip("192.127.0.2")
    # print(await data_base.is_ip_blocked("192.127.0.2"))
    # print(await data_base.get_permission("admin"))
    # print(await data_base.get_user("admin"))


if __name__ == '__main__':
    asyncio.run(run())
