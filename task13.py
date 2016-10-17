import random
import sys


def get_array(size):
    list1 = [0] * 10
    index = random.randint(0, size - 1)
    list1[index] = 1
    list1[get_index(index, size - 1)] = 1

    list1 = [x + get_index(1, 20) if x != 1 else 1 for x in list1]
    return list1


def get_index(ne, to=sys.maxsize):
    index = random.randint(0, to)
    return get_index(ne, to) if index == ne else index


if __name__ == "__main__":
    print(get_array(10))
