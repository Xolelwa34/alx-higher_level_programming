#!/usr/bin/python3

def add_arg(argv):
    ret = len(argv) - 1
    if ret == 0:
        print("{}".format(ret))
        return
    else:
        i = 1
        add = 0
        while i <= ret:
            add += int(argv[i])
            i += 1
        print("{}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
