from server import Server
import asyncio


# Запуск сервера
server = Server('localhost', 8881)
server.run()

