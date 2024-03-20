from my_error import ConverterError


class NumberConverter:

    def __init__(self):
        self.hexik = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C',
                      'D', 'E', 'F']
        self.binik = ['0', '1']
        self.decik = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.octik = ['0', '1', '2', '3', '4', '5', '6', '7']
        self.map_conv = {"bin_oct": self.binary_to_octal, "bin_dec": self.binary_to_decimal,
                    "bin_hex": self.binary_to_hexadecimal,
                    "oct_bin": self.octal_to_binary, "oct_dec": self.octal_to_decimal,
                    "oct_hex": self.octal_to_hexadecimal,
                    "dec_oct": self.decimal_to_octal, "dec_bin": self.decimal_to_binary,
                    "dec_hex": self.decimal_to_hexadecimal, "hex_oct": self.hexadecimal_to_octal,
                    "hex_bin": self.hexadecimal_to_binary, "hex_dec": self.hexadecimal_to_decimal}

    def binary_to_decimal(self, number):
        if not all(char in self.binik for char in str(number)):
            raise ConverterError
        return int(str(number), 2)

    def binary_to_octal(self, number):
        decimal_number = NumberConverter.binary_to_decimal(int(number))
        return oct(decimal_number)[2:]

    def binary_to_hexadecimal(self, number):
        decimal_number = NumberConverter.binary_to_decimal(int(number))
        return hex(decimal_number)[2:]

    def decimal_to_binary(self, number):
        if not all(char in self.decik for char in str(number)):
            raise ConverterError
        return bin(int(number))[2:]

    def decimal_to_octal(self, number):
        if not all(char in self.decik for char in str(number)):
            raise ConverterError
        return oct(int(number))[2:]

    def decimal_to_hexadecimal(self, number):
        if not all(char in self.decik for char in str(number)):
            raise ConverterError
        return hex(int(number))[2:]

    def octal_to_binary(self, number):
        if not all(char in self.octik for char in str(number)):
            raise ConverterError
        decimal_number = int(str(number), 8)
        return bin(decimal_number)[2:]

    def octal_to_decimal(self, number):
        if not all(char in self.octik for char in str(number)):
            raise ConverterError
        return int(str(number), 8)

    def octal_to_hexadecimal(self, number):
        if not all(char in self.octik for char in str(number)):
            raise ConverterError
        decimal_number = int(str(number), 8)
        return hex(decimal_number)[2:]

    def hexadecimal_to_binary(self, number):
        if not all(char in self.hexik for char in str(number)):
            raise ConverterError
        decimal_number = int(str(number), 16)
        return bin(decimal_number)[2:]

    def hexadecimal_to_decimal(self, number):
        if not all(char in self.hexik for char in str(number)):
            raise ConverterError
        return int(str(number), 16)

    def hexadecimal_to_octal(self, number):
        if not all(char in self.hexik for char in str(number)):
            raise ConverterError
        decimal_number = int(str(number), 16)
        return oct(decimal_number)[2:]

    words_map_conv = {"bin_oct": ["двоичной", "восьмиричную"], "bin_dec": ["двоичной", "десятиричную"],
                      "bin_hex": ["двоичной", "шестнадцатеричную"],
                      "oct_bin": ["восьмиричной", "двоичную"], "oct_dec": ["восьмиричной", "десятичную"],
                      "oct_hex": ["восьмиричной", "шестнадцатеричную"],
                      "dec_oct": ["десятиричной", "восьмиричную"], "dec_bin": ["десятиричной", "двоичную"],
                      "dec_hex": ["десятиричной", "шестнадцатеричную"],
                      "hex_oct": ["шестнадцатеричной", "восьмиричную"],
                      "hex_bin": ["шестнадцатеричной", "двоичную"], "hex_dec": ["шестнадцатеричной", "десятиричную"]}

    @staticmethod
    def hexadecimal_to_octal(number):
        decimal_number = int(str(number), 16)
        return oct(decimal_number)[2:]

# num = NumberConverter()
# args = ["dec", "bin", 2]
# if type(args[0]) == str and type(args[1]) == str and len(args) == 3:
#     operation = str(args[0]) + "_" + str(args[1])
#     if (operation in NumberConverter.map_conv.keys()) and args[2]:
#         print("Перевод числа {} из {} в {} систему: {}".format(args[2], *NumberConverter.words_map_conv[operation],
#                                                                NumberConverter.map_conv[operation](args[2])))
#     else:
#         print(2)
# # print(
# #         "Перевод числа {} из {} в {} систему: {}".format(args[0], *NumberConverter.words_map_conv[args],
# #                                                          NumberConverter.map_conv[args](args[0])))
