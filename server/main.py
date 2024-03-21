from server import Server
import asyncio


# Запуск сервера
server = Server('192.168.1.114', 8888)
server.run()

