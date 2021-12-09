from Usage import usage
import sys

def cut(args):
    """remove sections from each line of files"""
    if len(args) < 1:
        usage("Too few arguments", "cut")
        sys.exit(1)
    if args[0] == '-f':
        if len(args) < 3:
            usage("A comma-separated field specification is required", "cut")
            sys.exit(1)
        cols = args[1]
        args = args[2:]
        columns = cols.split(sep=",")
        #sort columns
        sortedColumns = []
        for x in columns:
            sortedColumns.append(int(x))
        sortedColumns.sort()                    #inputted columns are now sorted

        for i in args:                          #complete cut for each file
            f = open(i)
            for z in f.readlines():
                arr = z.split(sep=",")          #separate each line into its values
                for y in sortedColumns:         #print out each inputted columm
                    """print('hi')
                    print(y)
                    print(len(arr))
                    print('hi')"""
                    if y-1 >= len(arr):
                        print()
                    elif len(sortedColumns) <= 1:
                        print(arr[y-1], end="")
                        print()
                    elif sortedColumns.index(y) == len(sortedColumns)-1:
                        print(arr[y-1][0:-1], end="")
                    else:
                        print(arr[y-1] + ",", end="")
                        print()
            f.close()


    else:
        if len(args) < 1:
            usage("Too few arguments", "cut")
            sys.exit(1)
        for i in args:
            f = open(i)
            for x in f.readlines():
                arr = x.split(sep=",")
                print(arr[0])
            f.close()




    """*In cut, read each line of the CSV file as a string and call .split on it using a comma as the separator. This will
give us the desired strings or empty strings in the place of each file. Print out the 0th value in the array if "-f" isn't
called. If it is, split the inputted numbers into an array separated by commas as well. Loop through array finding the smallest
fth number and printing out that f-1th value of the array. Remove that value from array and repeat. Put all of it in a while len
is greater than 0 loop so no errors are thrown.
"""









def paste(args):
    """merge lines of files"""
    if len(args) == 0:
        usage("Too few arguments", "paste")
    largest = 0
    whichone = ""
    for i in args:
        f = open(i)
        currentN = 0
        currentF = str(i)
        for lines in f.readlines():          #count number of lines in each file
            currentN += 1
        if currentN > largest:              #if its the largest number of lines then set it to largest
            largest = currentN
            whichone = currentF
        f.close()

    for x in range(0, largest):
        lastprint = ""
        for i in args:
            f = open(i)
            curr = []
            for lines in f.readlines():
                curr.append(lines[0:-1])
            if x > len(curr)-1:
                if not args[-1] == i:
                    print(',', end="")
                    lastprint = ","
            else:
                if args[-1] == i:
                    print(curr[x], end="")
                    lastprint= curr[x]
                else:
                    print(curr[x] + ",", end="")
                    lastprint = curr[x] + ","
        print()





"""CUTPASTE.PY
Have a method called cut and a method called paste. In paste, open all files and set them to different variable names. Find the
file with the largest number of lines. Use that as the count for the loop. (for x in range [largest number of lines])
Within the loop print out the specific line in each file (variable.readline()). Readline also prints out an extra
line after that so make sure you account for that"""