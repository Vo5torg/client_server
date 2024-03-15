import asyncio
import json
from number_converter import NumberConverter
from client import Client

system_ = ["bin", "oct", "dec", "hex"]
while True:
    input_text = input().strip().split()
    command = input_text[0]
    param = input_text[1]
    args = input_text[2:]
    if "reg" in command:
        pass
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
