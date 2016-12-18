import re

INTEGER = '\d+'
OPERATION = '[+|\\-|/|*]'
OPEN_BR = '\(?'
CLOSE_BR = '\)?'
INTEGER_OPERATION = '%s%s%s' % (INTEGER, CLOSE_BR, OPERATION)
EXPRESSION = '(%s(?:%s%s)+)%s%s' % (OPEN_BR, INTEGER_OPERATION, OPEN_BR, INTEGER, CLOSE_BR)


def is_syntax_correct(input):
    print(EXPRESSION)
    pattern = re.compile(EXPRESSION)
    return not pattern.match(input) is None


if __name__ == '__main__':
    test_expressions = ["23-", "2-3(", ")2-34", "2(-)34", "(2-)34"]
    for i in test_expressions:
        print(is_syntax_correct(i))
