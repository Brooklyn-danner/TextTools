from Usage import usage
import sys

def grep(args):
    """print lines that match patterns"""
    if len(args) == 0:
        usage("Please provide a pattern and at least one filename", "grep")
        sys.exit(1)

    if args[0] == "-v":
        if len(args) < 3:
            usage("Please provide a pattern and at least one filename", "grep")
            sys.exit(1)
        word = args[1]
        args = args[2:]
        for i in args:
            f = open(i)
            for lines in f.readlines():
                if not word in lines:
                    print(lines, end="")
            f.close()
    else:
        word = args[0]
        if len(args) == 1:
            usage("Please provide a pattern and at least one filename", "grep")
            sys.exit(1)
        args = args[1:]
        for i in args:
            f = open(i)
            for lines in f.readlines():
                if word in lines:
                    print(lines, end="")
            f.close()

""" First check to see if "-v" is used when calling grep.
If not:
*       Loop through each file by using readlines() function. In that loop, read the string that accompanies each readlines
iteration by using if s in str boolean call. If that line contains it, print it out.
If yes:
*       Do the same thing as above, except if s in str = false then print out the string.

also its put in as grep -v [word] [files]
"""