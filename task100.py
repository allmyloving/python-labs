START_CYRILLIC_CODE = 1040


def cipher(message):
    if len(message) % 2 != 0:
        message += ' '
    return [code(message[i]) << 6 | code(message[i + 1]) for i in range(0, len(message) - 1, 2)]


def code(char):
    return 0 if char.isspace() else ord(char) - START_CYRILLIC_CODE + 1


def char(code):
    return ' ' if not code else chr(code + START_CYRILLIC_CODE - 1)


# 0x3F is 0b111111
def decipher(message):
    print(message[3] >> 6)
    print(message[3] & 0x3F)
    return ''.join((char(i >> 6) + char(i & 0x3F)) for i in message)


if __name__ == "__main__":
    print(decipher(cipher('СЕРВЕРЗ')))
