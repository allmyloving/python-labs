# Проверить валидность арифметического выражения
import re

INTEGER = '\d+'
OPERATION = '[+|\\-|/|*]'
OPEN_BR = '\(?'
CLOSE_BR = '\)?'
INTEGER_OPERATION = '%s%s%s' % (INTEGER, CLOSE_BR, OPERATION)
EXPRESSION = '(%s(?:%s%s)+)%s%s' % (OPEN_BR, INTEGER_OPERATION, OPEN_BR, INTEGER, CLOSE_BR)


def is_expression_valid(input):
    return is_syntax_valid(input) and are_brackets_valid(input)


def is_syntax_valid(input):
    pattern = re.compile(EXPRESSION)
    return not pattern.match(input) is None


def are_brackets_valid(input):
    stack = []
    for i in input:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    invalid_expressions = ["23-", "2)+2*(3", "2-3(", ")2-34", "2(-)34", "(2-)34", ")(5+1()", ")1-2(", "((1)))(", "(1+1)+1"]
    for i in invalid_expressions:
        print("%s is valid: %r" % (i, is_expression_valid(i)))

    valid_expressions = ["2+3+56", "12*2/8", "12*(12-10)", "(8+4)*10-(22+3)"]
    for i in valid_expressions:
        print("%s is valid: %r" % (i, is_expression_valid(i)))
