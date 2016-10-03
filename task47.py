class BigNum:
    @staticmethod
    def to_list(num):
        list = []
        div = 10
        while num > 0:
            list.insert(0, num % div)
            num = int(num / 10)
        return list

    def __init__(self, num):
        self.value = BigNum.to_list(num)

    def mul(self, num):
        mul = BigNum.to_list(num)
        result = [0] * (len(self.value) + len(mul) + 1)

        for i in range(len(mul)):
            carry = 0
            k = len(result) - 1
            for j in range(len(self.value) - 1, -1, -1):
                calc = self.value[j] * mul[len(mul) - i - 1]
                temp = result[k - i] + calc + carry
                if temp >= 10:
                    carry = int(temp / 10)
                    temp %= 10
                else:
                    carry = 0
                result[k - i] = temp
                k -= 1
            if carry != 0 and result[k - i] == 0:
                result[k - i] = carry

        result[0:BigNum.get_zero_index(result)] = []
        self.value = result

    @staticmethod
    def get_zero_index(list):
        for index in range(len(list)):
            if list[index] != 0:
                return index

    def get_digit_matrix(self):
        matrix = [0] * 10
        for element in self.value:
            matrix[element] += 1
        return matrix

    def __str__(self):
        result = ""
        for i in self.value:
            result += str(i)
        return result

def factorial_numbers():
    num = BigNum(1)
    for i in range(1, 101):
        num.mul(i)
    print("100! is {0}".format(num))
    print(num.get_digit_matrix())


if __name__ == "__main__":
    factorial_numbers()
