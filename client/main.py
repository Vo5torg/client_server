import asyncio
import argparse
from number_converter import NumberConverter
from client import Client
from my_error import *

parser = argparse.ArgumentParser(description='convertor of number systems')
parser.add_argument('port', type=int, help='server_port')
parser.add_argument('id', type=int, help='client_id')
args = parser.parse_args()

client = Client("localhost", args.port, args.id)
print("Введите команду 'info' чтобы узнать что делать.")
meow = True
nums_conv = NumberConverter()
while meow:
    try:
        input_text = input("Введите команду: ").strip().split()
        command = input_text[0]
        args = input_text[1:]
        if "info" in command:
            print("Эта программа написана для перевода чисел в различные системы счисления.\n"
                  "Список команд:\n"
                  "\t\t\t info - посмотреть общую информацию\n"
                  "\t\t\t reg {login} {password} - регистрация\n"
                  "\t\t\t auth {login} {password} - авторизация\n"
                  "\t\t\t conv {from num sys} {to num sys} {num} - перевод чисел\n"
                  "\t\t\t Системы счислений: bin, oct, dec, hex.\n"
                  "\t\t\t my_perm - посмотреть права\n"
                  "Для администратора:\n"
                  "\t\t\t set_perm {login} {num_sys} {value} - изменить права\n"
                  "\t\t\t show_users - посмотреть всех пользователей\n"
                  "\t\t\t show_ip - показать заблокированные ip\n"
                  "\t\t\t block_ip {ip} - заблокировать ip\n"
                  "\t\t\t allow_ip {ip} - разблокировать ip\n")
        elif "reg" in command:
            if len(args) == 2:
                response = asyncio.run(client.registration(args[0], args[1]))
                print(f"Пользователь {args[0]} зарегистрирован!")
            else:
                raise InputError
        elif "auth" in command:
            if len(args) == 2:
                response = asyncio.run(client.authorization(args[0], args[1]))
                if response.status:
                    if response.is_admin:
                        print(f"Вы успешно авторизировались за админа {args[0]}!")
                    else:
                        print(f"Вы успешно авторизировались за пользователя {args[0]}!")
                else:
                    print("Что-то пошло не по плану. Авторизация за этого пользователя не удалась.")
            else:
                raise InputError
        elif "conv" in command:
            response = asyncio.run(client.get_permission())
            if type(args[0]) == str and type(args[1]) == str and len(args) == 3:
                perm = {"bin": (True if str(response.other_data[2]).lower() in ["true", "1"] else False),
                        "oct": (True if str(response.other_data[3]).lower() in ["true", "1"] else False),
                        "dec": (True if str(response.other_data[4]).lower() in ["true", "1"] else False),
                        "hex": (True if str(response.other_data[5]).lower() in ["true", "1"] else False)}
                operation = str(args[0]) + "_" + str(args[1])
                if (operation in nums_conv.map_conv.keys()) and args[2]:
                    if perm.get(args[0]):
                        if perm.get(args[1]):
                            print("Перевод числа {} из {} в {} систему: {}".format(args[2],
                                                                                   *nums_conv.words_map_conv[
                                                                                       operation],
                                                                                   nums_conv.map_conv[operation](
                                                                                       args[2])))
                        else:
                            print(f"У вас нет прав для использования {args[1]}")
                    else:
                        print(f"У вас нет прав для использования {args[0]}")
                else:
                    print("Ошибка! Пример команды для перевода числа из десятичной в двоичную: conv dec bin 2")
            else:
                print("Ошибка! Пример команды для перевода числа из десятичной в двоичную: conv dec bin 2")
        elif "my_perm" in command:
            response = asyncio.run(client.get_permission())
            print(
                f"Права: bin {True if response.other_data[2] else False} ; "
                f"oct: {True if response.other_data[3] else False}; "
                f"dec: {True if response.other_data[4] else False}; "
                f"hex: {True if response.other_data[5] else False}; ")
        elif "set_perm" in command:
            if len(args) == 3:
                response = asyncio.run(client.set_permission(args[0], args[1], args[2]))
                print(f"Значение {args[2]} для системы счисления {args[1]} у пользователя {args[0]} установлено.")
            else:
                raise InputError
        elif "show_users" in command:
            response_user = asyncio.run(client.get_users())
            users_list = response_user.other_data
            if users_list:
                for num, user_info in enumerate(users_list):
                    response_perm = asyncio.run(client.get_permission(user_info[1])).other_data
                    print(
                        f"{num}) Пользователь: {user_info[1]}; "
                        f"Права администратора {True if user_info[3] else False}; "
                        f"Ip: {user_info[4]}; Права: bin {True if response_perm[2] else False} ; oct:"
                        f" {True if response_perm[3] else False}; dec: {True if response_perm[4] else False}; "
                        f"hex: {True if response_perm[5] else False};\n")
            else:
                raise Exception
        elif "show_ip" in command:
            response = asyncio.run(client.get_block_ip())
            ip_list = response.other_data
            if ip_list:
                for num, ip in enumerate(ip_list):
                    print(f"\n{num}) Ip: {ip[1]}")
            else:
                raise Exception
        elif "block_ip" in command:
            if len(args) == 1:
                response = asyncio.run(client.block_ip(args[0]))
                print(f"Ip адрес {args[0]} заблокирован!")
            else:
                raise InputError
        elif "allow_ip" in command:
            if len(args) == 1:
                response = asyncio.run(client.allow_ip(args[0]))
                print(f"Ip адрес {args[0]} разблокирован!")
            else:
                raise InputError
        else:
            raise InputError
    except AuthorizationError:
        print("Ошибка при авторизации!!! Попробуйте ввести другие данные.")
    except RegistrationError:
        print("Ошибка при регистрации!!!Возможно такой пользователь существует.")
    except InputError:
        print("Неверная команда или параметры. Введите 'info'")
    except NoAdmin:
        print("Похоже команда которую вы хотите использовать доступна только админу.")
    except IpBlocked:
        print("Ваш айпи заблокирован!!.")
    except NotAuthorized:
        print("Эта команда доступна только авторизированным пользователям.")
    except ConverterError:
        print("Ошибка при конвертации, удостоверьтесь что правильно выбрали систему счисления.")
    except KeyboardInterrupt:
        print("\nПока!")
        meow = False
    except Exception as Ex:
        print("Похоже возникла непредвиденная ошибка.")
        print(Ex)
