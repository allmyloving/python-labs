def string_range(list, length):
    for i in list:
        if len(i) == length:
            yield i


if __name__ == '__main__':
    strings = ["asdf", "asd", "string", "str"]
    for value in string_range(strings, 4):
        print(value)

    print(list(string_range(strings, 3)))
