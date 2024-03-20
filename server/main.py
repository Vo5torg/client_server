from server import Server
import asyncio


# Запуск сервера
server = Server('localhost', 8882)
server.run()

