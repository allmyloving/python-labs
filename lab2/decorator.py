# Декоратор для обработки исключений (поймать исключение из функции и выбросить общее наружу)
class ApiException(Exception):
    def __init__(self, status):
        self.status = status

    def __str__(self):
        return repr(self.status)


def exception_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print("The following exception occurred={0}, cause={1}".format(error, error.__cause__))
            raise ApiException(500)

    return inner


@exception_handler
def divide(a, b):
    return a / b


if __name__ == '__main__':
    divide(1, 0)
