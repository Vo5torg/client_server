import asyncio
import json
from number_converter import NumberConverter
from client import Client

system_ = ["bin", "oct", "dec", "hex"]

client = Client('localhost', 8881, 1)
# asyncio.run(client.send_message("11"))
functions = {"reg": registration, "auth": authorization, "get": get_permission,
                          "set": set_permission, "show_users": block_ip, "block_ip": block_ip,
                          "allow_ip": allow_ip}
while True:
    try:
        input_text = input().strip().split()
        command = input_text[0]
        param = input_text[1]
        args = input_text[2:]
        if "reg" in command:
            asyncio.run(client.send_message({'action': "reg"}))
        elif "auth" in command:
            pass
        elif "conv" in command:
            if param in NumberConverter.map_conv.keys():
                print("Перевод числа {} из {} в {} систему: {}".format(args[0], *NumberConverter.words_map_conv[param],
                                                                       NumberConverter.map_conv[param](args[0])))
        elif "info" in command:
            pass
        elif "perm" in command:
            pass
        elif "set" in command:
            pass
        else:
            print("Неверная команда или параметры.")
    except:
        pass
