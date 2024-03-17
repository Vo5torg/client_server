class NumberConverter:

    @staticmethod
    def binary_to_decimal(number):
        return int(str(number), 2)

    @staticmethod
    def binary_to_octal(number):
        decimal_number = NumberConverter.binary_to_decimal(int(number))
        return oct(decimal_number)[2:]

    @staticmethod
    def binary_to_hexadecimal(number):
        decimal_number = NumberConverter.binary_to_decimal(int(number))
        return hex(decimal_number)[2:]

    @staticmethod
    def decimal_to_binary(number):
        return bin(int(number))[2:]

    @staticmethod
    def decimal_to_octal(number):
        return oct(int(number))[2:]

    @staticmethod
    def decimal_to_hexadecimal(number):
        return hex(int(number))[2:]

    @staticmethod
    def octal_to_binary(number):
        decimal_number = int(str(number), 8)
        return bin(decimal_number)[2:]

    @staticmethod
    def octal_to_decimal(number):
        return int(str(number), 8)

    @staticmethod
    def octal_to_hexadecimal(number):
        decimal_number = int(str(number), 8)
        return hex(decimal_number)[2:]

    @staticmethod
    def hexadecimal_to_binary(number):
        decimal_number = int(str(number), 16)
        return bin(decimal_number)[2:]

    @staticmethod
    def hexadecimal_to_decimal(number):
        return int(str(number), 16)

    @staticmethod
    def hexadecimal_to_octal(number):
        decimal_number = int(str(number), 16)
        return oct(decimal_number)[2:]

    map_conv = {"bin_oct": binary_to_octal, "bin_dec": binary_to_decimal,
                "bin_hex": binary_to_hexadecimal,
                "oct_bin": octal_to_binary, "oct_dec": octal_to_decimal,
                "oct_hex": octal_to_hexadecimal,
                "dec_oct": decimal_to_octal, "dec_bin": decimal_to_binary,
                "dec_hex": decimal_to_hexadecimal, "hex_oct": hexadecimal_to_octal,
                "hex_bin": hexadecimal_to_binary, "hex_dec": hexadecimal_to_decimal}

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
