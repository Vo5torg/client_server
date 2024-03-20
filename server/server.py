import asyncio
import json
from database import AsyncDataBase
from protocol import Protocol


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.db = AsyncDataBase()
        self.functions = {"reg": self.registration, "auth": self.authorization, "get": self.get_permission,
                          "set": self.set_permission, "show_users": self.get_users, "block_ip": self.block_ip,
                          "allow_ip": self.allow_ip, "show_ip": self.show_block_ip}

    def run(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.start())
        except KeyboardInterrupt:
            print("Server interrupted")
        except Exception as Ex:
            print(Ex)
        finally:
            self.stop()
            loop.close()

    async def start(self):
        try:
            server = await asyncio.start_server(self.handle_request, self.host, self.port)
            addr = server.sockets[0].getsockname()
            print(f'Serving on {addr}')

            async with server:
                await server.serve_forever()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def stop(self):
        if self.server:
            self.server.close()

    async def handle_request(self, reader, writer):

        addr = writer.get_extra_info('peername')
        print("Подключился: ", addr)
        data = await reader.read(1024)
        request = json.loads(data.decode())
        request["ip"] = addr[0]
        request["port"] = addr[1]
        response_json = await self.process_request(request)
        writer.write(json.dumps(response_json).encode())
        await writer.drain()
        writer.close()

    async def process_request(self, request_json):

        request = Protocol(request_json)
        pre_response = {
            "message_id": request.message_id + 1,
            "client_id": request.client_id,
            "action": request.action
        }
        response = Protocol(pre_response)
        if not await self.db.is_ip_blocked(request.ip):
            response = await self.functions.get(request.action)(request, response)
            response.ip_blocked = False
        else:
            response.ip_blocked = True
            response.status = False
        return response.dict_json

    async def registration(self, req, res):
        print(f"Запрос на регистрация пользователя: {req.login}, ip/port: {req.ip}/{req.port}")
        if not (req.login and req.password):
            res.status = False
        else:
            result = await self.db.add_user(req.login, req.password, False, req.ip)
            res.status = result
        return res

    async def authorization(self, req, res):
        print(f"Запрос на авторизацию пользователя: {req.login}, ip/port: {req.ip}/{req.port}")
        if not (req.login and req.password):
            res.status = False
        else:
            user = await self.db.get_user(req.login)
            admin = await self.db.is_admin(req.login)
            if user:
                if user[2] == req.password:
                    if admin:
                        res.is_admin = True
                    res.status = True
                else:
                    res.status = False
            else:
                res.status = False
        return res

    async def get_permission(self, req, res):
        print(f"Запрос разрешений пользователем: {req.login}, ip/port: {req.ip}/{req.port}")
        perm = await self.db.get_permission(req.login)
        if perm:
            res.status = True
            res.other_data = perm
        else:
            res.status = False
        return res

    async def set_permission(self, req, res):
        print(f"Запрос на изменение прав: {req.login}, ip/port: {req.ip}/{req.port}")
        admin = await self.db.is_admin(req.login)
        if admin:
            res.is_admin = True
            result = await self.db.set_permission(req.other_data["user_login"], req.other_data["option"],
                                                  req.other_data["value"])
            if result:
                res.status = True
            else:
                res.status = False
        else:
            res.is_admin = False
            res.status = False
        return res

    async def get_users(self, req, res):
        print(f"Запрос списка пользователей админом: {req.login}, ip/port: {req.ip}/{req.port}")
        admin = await self.db.is_admin(req.login)
        if admin:
            res.is_admin = True
            users_list = await self.db.get_users()
            if users_list:
                res.other_data = users_list
                res.status = True
            else:
                res.status = False
        else:
            res.is_admin = False
            res.status = False
        return res

    async def show_block_ip(self, req, res):
        print(f"Запрос на список заблокированных айпи админом: {req.login}, ip/port: {req.ip}/{req.port}")
        admin = await self.db.is_admin(req.login)
        if admin:
            res.is_admin = True
            result = await self.db.show_block_ip()
            if result:
                res.other_data = result
                res.status = True
            else:
                res.status = False
        else:
            res.is_admin = False
            res.status = False
        return res

    async def block_ip(self, req, res):
        print(f"Запрос на блокировку айпи {req.other_data} админом: {req.login}, ip/port: {req.ip}/{req.port}")
        admin = await self.db.is_admin(req.login)
        if admin:
            res.is_admin = True
            result = await self.db.block_ip(req.other_data)
            if result:
                res.status = True
            else:
                res.status = False
        else:
            res.is_admin = False
            res.status = False
        return res

    async def allow_ip(self, req, res):
        print(f"Запрос разблокировку айпи {req.other_data} админом: {req.login}, ip/port: {req.ip}/{req.port}")
        admin = await self.db.is_admin(req.login)
        if admin:
            res.is_admin = True
            result = await self.db.allow_ip(req.other_data)
            if result:
                res.status = True
            else:
                res.status = False
        else:
            res.is_admin = False
            res.status = False
        return res
