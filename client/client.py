import asyncio
import json
import random


class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.id = 1

    async def run_client(self, message):
        reader, writer = await asyncio.open_connection(self.server_host, self.server_port)
        writer.write(json.dumps(message).encode())
        await writer.drain()
        response = await reader.read(1024)
        print(f'Response: {json.loads(response.decode())}')

        writer.close()
        await writer.wait_closed()


def read_json():
    with open("data.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data


def dumb_json(data):
    with open("data.json", "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, ensure_ascii=False)


info_client = {
    "client_id": 1,
    "admim": False,
    "login": "",
    "password": "",
    "allowed_operations": {"bin-oct": True, "bin-dec": True, "bin-hex": True, "oct-bin": True,
                           "oct-dec": True,
                           "oct-hex": True, "dec-oct": True, "dec-bin": True, "dec-hex": True,
                           "hex-oct": True,
                           "hex-bin": True, "hex-dec": True}

}

protocol = {
    "response": {
        "user_id": "",
        "action": ""
    },
    "request": {},
    "user_id": "",
    "action": ["reg", "auth", "get", "set"],
    "error": ""
}
client = Client('localhost', 8881)
asyncio.run(client.run_client("11"))
