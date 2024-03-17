import asyncio
import json
from server_protocol import RequestForServer, ResponseForServer


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None

    async def handle_request(self, reader, writer):

        addr = writer.get_extra_info('peername')
        print("Подключился: ", addr)
        data = await reader.read(1024)
        request = RequestForServer(json.loads(data.decode()))
        # Обработка запроса на стороне сервера
        response = self.process_request(request)
        writer.write(json.dumps(response).encode())
        await writer.drain()
        writer.close()

    def process_request(self, request):
        response = ResponseForServer()
        return response

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

    def run(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.start())
        except KeyboardInterrupt:
            print("Server interrupted")
        finally:
            self.stop()
            loop.close()
