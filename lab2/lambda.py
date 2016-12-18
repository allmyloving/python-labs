def to_fahrenheit(grads):
    return list(map(lambda x: x * 9 / 5 + 32, grads))


if __name__ == '__main__':
    grads = [0, 12, 20, -5]
    print(to_fahrenheit(grads))
