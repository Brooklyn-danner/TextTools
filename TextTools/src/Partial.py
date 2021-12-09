from Usage import usage
import sys

def head(args):
    """output the first part of files"""
    if len(args) == 0:
        usage("Too few arguments", "head")
        sys.exit(1)
    banner = False
    if not args[0] == '-n':
        if len(args) > 1:
            banner = True
        for i in args:
            f = open(i)
            if banner:
                print('==>' + i + '<==')
            for x in range(1, 11):
                print(f.readline(), end="")
            f.close()
            print()
    else:
        if len(args) == 1:
            usage("Number of lines is required", "head")
            sys.exit(1)
        if not args[1].isdigit():
            usage("Number of lines is required", "head")
            sys.exit(1)
        n = int(args[1])
        args = args[2:]
        if len(args) > 1:
            banner = True
        for i in args:
            f = open(i)
            if banner:
                print('==> ' + i + ' <==')
            for x in range(1, n+1):
                print(f.readline(), end="")
            f.close()
            print()


def tail(args):
    """output the last part of files"""
    if len(args) == 0:
        usage("Too few arguments", "tail")
        sys.exit(1)
    banner = False
    if not args[0] == '-n':
        if len(args) > 1:
            banner = True
            # loop through files
        for i in args:
            f = open(i)
            if banner:
                print('==> ' + i + ' <==')
            arr = []
            for lines in f.readlines():
                arr.append(lines[0:-1])
            # if f.lines <=10 print it all out
            if len(arr) <= 10:
                for l in arr:
                    print(l)
            # if f.lines > 10 print out only last 10
            else:
                arr = arr[-10:]
                for l in arr:
                    print(l)
                f.close()
                print()
    else:
        if len(args) == 1:
            usage("Number of lines is required", "head")
            sys.exit(1)
        if not args[1].isdigit():
            usage("Number of lines is required", "head")
            sys.exit(1)
        n = int(args[1])
        args = args[2:]
        if len(args) > 1:
            banner = True
        #loop through files
        for i in args:
            f = open(i)
            if banner:
                print('==> ' + i + ' <==')
            arr = []
            for lines in f.readlines():
                arr.append(lines[0:-1])
            # if f.lines <=n print it all out
            if len(arr) <= n:
                for l in arr:
                    print(l)
            # if f.lines > n print out only last 10
            else:
                arr=arr[n*-1:]
                for l in arr:
                    print(l)
            f.close()
            print()




# make sure I'm closing the files correctly

"""* Two methods:
*       Head- Check to see if -n was called with the function. If not, use a "for x in range 10" loop to iterate. In
each iteration print .readline() but be careful about the
extra line at the end when readline is called. If -n was called, simply switch to using for x in range n.
*       Tail- Read in the file using open() and load it into an array. Use str.split(sep = "\n"). Then, loop through the array backwar>
times. If "-v" is called, print content of array v times.
* Take into consideration if v is longer than contents of file. Call usage if so.
"""









"""Correct output:
 $ python src/tt.py head -n 3 data/ages8 data/names8 data/words200
    ==> data/ages8 <==
    Age
    22
    36

    ==> data/names8 <==
    Name
    Adrianna
    Julian

    ==> data/words200 <==
    social
    insomniac
    implicitly


    $ python src/tt.py head -n 3 data/complexity data/debugging
    ==> data/complexity <==
         "There are two ways of constructing a software design:

                    one way is to make it so simple

    ==> data/debugging <==
            "Everyone knows that debugging is twice as hard
                as writing a program in the first place.
"""