import asyncio
import json
from protocol import Protocol
from my_error import *


class Client:
    def __init__(self, server_host, server_port, client_id):
        self.server_host = server_host
        self.server_port = server_port
        self.authorized = False
        self.login = None
        self.message_id = 0
        self.client_id = client_id

    async def send_message(self, request):
        request.message_id = self.message_id
        request.client_id = self.client_id
        reader, writer = await asyncio.open_connection(self.server_host, self.server_port)
        writer.write(json.dumps(request.dict_json).encode())
        await writer.drain()
        response_encoding = await reader.read(1024)
        response_json = json.loads(response_encoding.decode())
        self.message_id += 1
        response = Protocol(response_json)
        # print(f'Response: {response_json}')
        writer.close()
        await writer.wait_closed()
        if response.ip_blocked:
            raise IpBlocked
        return response

    async def registration(self, login, password):
        req = Protocol({})
        req.action = "reg"
        req.login = login
        req.password = password
        res = await self.send_message(req)
        if res.status:
            return res
        else:
            raise RegistrationError

    async def authorization(self, login, password):
        req = Protocol({})
        req.action = "auth"
        req.login = login
        req.password = password
        res = await self.send_message(req)
        if res.status:
            self.authorized = True
            self.login = login
            return res
        else:
            raise AuthorizationError

    async def get_permission(self, user_login=None):
        req = Protocol({})
        req.action = "get"
        if user_login:
            req.login = user_login
        else:
            req.login = self.login
        res = await self.send_message(req)
        if not self.authorized:
            raise NotAuthorized
        if res.status:
            return res
        else:
            raise Exception

    async def set_permission(self, user_login, option, value):
        req = Protocol({})
        req.action = "set"
        req.login = self.login
        req.other_data = {}
        req.other_data["user_login"] = user_login
        req.other_data["option"] = option
        req.other_data["value"] = value
        res = await self.send_message(req)
        if not self.authorized:
            raise NotAuthorized
        if not res.is_admin:
            raise NoAdmin
        if res.status:
            return res
        else:
            raise Exception

    async def get_users(self):
        req = Protocol({})
        req.action = "show_users"
        req.login = self.login
        res = await self.send_message(req)
        if not self.authorized:
            raise NotAuthorized
        if not res.is_admin:
            raise NoAdmin
        if res.status:
            return res
        else:
            raise Exception

    async def get_block_ip(self):
        req = Protocol({})
        req.action = "show_ip"
        req.login = self.login
        res = await self.send_message(req)
        if not self.authorized:
            raise NotAuthorized
        if not res.is_admin:
            raise NoAdmin
        if res.status:
            return res
        else:
            raise Exception

    async def block_ip(self, ip):
        req = Protocol({})
        req.action = "block_ip"
        req.login = self.login
        req.other_data = ip
        res = await self.send_message(req)
        if not self.authorized:
            raise NotAuthorized
        if not res.is_admin:
            raise NoAdmin
        if res.status:
            return res
        else:
            raise Exception

    async def allow_ip(self, ip):
        req = Protocol({})
        req.action = "allow_ip"
        req.login = self.login
        req.other_data = ip
        res = await self.send_message(req)
        if not self.authorized:
            raise NotAuthorized
        if not res.is_admin:
            raise NoAdmin
        if res.status:
            return res
        else:
            raise Exception

    @staticmethod
    def str_true(value):
        return True if str(value).lower() in ["true", "1"] else False
