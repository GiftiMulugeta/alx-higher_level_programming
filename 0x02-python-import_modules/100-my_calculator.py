#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) <= 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif len(sys.argv) > 3:
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(sys.argv[1], sys.argv[3],
                  add(int(sys.argv[1]), int(sys.argv[3]))))
            exit(0)
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(sys.argv[1], sys.argv[3],
                  sub(int(sys.argv[1]), int(sys.argv[3]))))
            exit(0)
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(sys.argv[1], sys.argv[3],
                  mul(int(sys.argv[1]), int(sys.argv[3]))))
            exit(0)
        elif sys.argv[2] == '/':
            print("{} / {} = {}".format(sys.argv[1], sys.argv[3],
                  div(int(sys.argv[1]), int(sys.argv[3]))))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
