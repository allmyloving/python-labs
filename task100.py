START_CYRILLIC_CODE = 1040


def get_code(char):
    code = 0 if char.isspace() else ord(char) - START_CYRILLIC_CODE + 1
    return to_binary6(code)


def to_binary6(decimal):
    return "{0:06b}".format(decimal)


def to_binary12(decimal):
    return "{0:012b}".format(decimal)


def to_decimal(binary):
    return int(binary, 2)


def cipher(message):
    result = []
    for i in range(0, len(message) - 1, 2):
        binary = get_code(message[i]) + get_code(message[i + 1])
        result.append(to_decimal(binary))
    return result


def get_char(binary):
    return chr(to_decimal(binary) + START_CYRILLIC_CODE - 1)


def decipher(message):
    result = ""
    for i in message:
        binary = to_binary12(i)
        middle = int(len(binary) / 2)
        result += get_char(binary[0:middle]) + get_char(binary[middle:len(binary)])
    return result


if __name__ == "__main__":
    # consider odd word length
    print(decipher(cipher('СЕРВЕРР')))
