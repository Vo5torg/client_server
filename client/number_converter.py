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

    map_conv = {"bin-oct": binary_to_octal, "bin-dec": binary_to_decimal,
                "bin-hex": binary_to_hexadecimal,
                "oct-bin": octal_to_binary, "oct-dec": octal_to_decimal,
                "oct-hex": octal_to_hexadecimal,
                "dec-oct": decimal_to_octal, "dec-bin": decimal_to_binary,
                "dec-hex": decimal_to_hexadecimal, "hex-oct": hexadecimal_to_octal,
                "hex-bin": hexadecimal_to_binary, "hex-dec": hexadecimal_to_decimal}

    words_map_conv = {"bin-oct": ["двоичной", "восьмиричную"], "bin-dec": ["двоичной", "десятиричную"],
                      "bin-hex": ["двоичной", "шестнадцатеричную"],
                      "oct-bin": ["восьмиричной", "двоичную"], "oct-dec": ["восьмиричной", "десятичную"],
                      "oct-hex": ["восьмиричной", "шестнадцатеричную"],
                      "dec-oct": ["десятиричной", "восьмиричную"], "dec-bin": ["десятиричной", "двоичную"],
                      "dec-hex": ["десятиричной", "шестнадцатеричную"],
                      "hex-oct": ["шестнадцатеричной", "восьмиричную"],
                      "hex-bin": ["шестнадцатеричной", "двоичную"], "hex-dec": ["шестнадцатеричной", "десятиричную"]}

    @staticmethod
    def hexadecimal_to_octal(number):
        decimal_number = int(str(number), 16)
        return oct(decimal_number)[2:]
