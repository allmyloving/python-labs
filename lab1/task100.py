START_CYRILLIC_CODE = 1040


def cipher(message):
    # add redundant space sign if the input has odd length
    if len(message) % 2 != 0:
        message += ' '
    return [code(message[i]) << 6 | code(message[i + 1]) for i in range(0, len(message) - 1, 2)]


# get char code relative to cyrillic alphabet
def code(char):
    return 0 if char.isspace() else ord(char) - START_CYRILLIC_CODE + 1


# get unicode char for given relative to cyrillic code
def char(code):
    return ' ' if not code else chr(code + START_CYRILLIC_CODE - 1)


# 0x3F is 0b111111
def decipher(message):
    print(message[3] >> 6)
    print(message[3] & 0x3F)
    return ''.join((char(i >> 6) + char(i & 0x3F)) for i in message)


if __name__ == "__main__":
    print(decipher(cipher('СЕРВЕРЗ')))
