#!/usr/bin/python3
# 2-args.py
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    ret = len(sys.argv) - 1
    if ret == 0:
        print("0 arguments.")
    elif ret == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ret))
    for i in range(ret):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
