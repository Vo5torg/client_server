import asyncio
import json
import random


class Client:
    def __init__(self, server_host, server_port, client_id):
        self.server_host = server_host
        self.server_port = server_port
        self.authorized = False
        self.message_id = 1
        self.client_id = client_id

    async def run_client(self, message):
        reader, writer = await asyncio.open_connection(self.server_host, self.server_port)
        writer.write(json.dumps(message).encode())
        await writer.drain()
        response = await reader.read(1024)
        print(f'Response: {json.loads(response.decode())}')
        writer.close()
        await writer.wait_closed()


info_client = {
    "client_id": 1,
    "admim": False,
    "login": "",
    "allowed_operations": {"bin": True, "oct": True, "dec": True, "hex": True}
}

protocol = {
    "action": ["reg", "auth", "get", "set", "get_users", "block_ip"],
}
