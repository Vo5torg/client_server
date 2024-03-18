import asyncio
import json
import random
from protocol import Protocol


class Client:
    def __init__(self, server_host, server_port, client_id):
        self.server_host = server_host
        self.server_port = server_port
        self.authorized = False
        self.message_id = 0
        self.client_id = client_id

    async def send_message(self, message):
        reader, writer = await asyncio.open_connection(self.server_host, self.server_port)
        writer.write(json.dumps(message).encode())
        await writer.drain()
        response_encoding = await reader.read(1024)
        response = json.loads(response_encoding.decode())
        print(f'Response: {response}')
        writer.close()
        await writer.wait_closed()

    async def process_request(self, request_json):
        pass


info_client = {
    "client_id": 1,
    "admim": False,
    "login": "",
    "allowed_operations": {"bin": True, "oct": True, "dec": True, "hex": True}
}

protocol = {
    "action": ["reg", "auth", "get", "set", "show_users", "block_ip"],
}
