import random
import sys


# create an array of random numbers with exactly two 1's of given size
def get_array(size):
    list1 = [0] * 10
    index = random.randint(0, size - 1)
    list1[index] = 1
    list1[get_index(index, size - 1)] = 1

    list1 = [get_index(1, 20) if x != 1 else 1 for x in list1]
    return list1


# get first index that doesn't equal 'ne' parameter, up to 'to'
def get_index(ne, to=sys.maxsize):
    index = random.randint(0, to)
    return get_index(ne, to) if index == ne else index


if __name__ == "__main__":
    print(get_array(10))
