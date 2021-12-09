from Usage import usage
import sys

def cat(args):
    """concatenate files and print on the standard output"""
    if len(args) == 0:
        usage("Too few arguments", "cat")
        sys.exit(1)

    for i in args:
        f = open(i)
        for lines in f.readlines():
            print(lines, end="")
        f.close()

def tac(args):
    """concatenate and print files in reverse"""
    if len(args) == 0:
        usage("Too few arguments", "grep")
        sys.exit(1)
    for i in args:
        rev = []
        f = open(i)
        for lines in f.readlines():
            rev.append(lines[0:-1])
        for l in range(len(rev)-1, -1, -1):
            print(rev[l])
        #loop backwards through rev

