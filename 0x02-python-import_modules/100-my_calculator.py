#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def arg_calc(argv):
    ret = len(argv) - 1
    if ret != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    oper = argv[2]
    b = int(argv[3])
    if oper == '+':
        print("{} {} {} = {}".format(a, oper, b, add(a, b)))
    elif oper == '-':
        print("{} {} {} = {}".format(a, oper, b, sub(a, b)))
    elif oper == '*':
        print("{} {} {} = {}".format(a, oper, b, mul(a, b)))
    elif oper == '/':
        print("{} {} {} = {}".format(a, oper, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    arg_calc(sys.argv)
