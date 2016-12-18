def celsius_to_fahrenheit(grad):
    return grad * 9 / 5 + 32


def to_fahrenheit(grads):
    return list(map(celsius_to_fahrenheit, grads))


if __name__ == '__main__':
    grads = [0, 12, 20, -5]
    print(to_fahrenheit(grads))
