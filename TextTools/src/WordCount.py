from Usage import usage
import sys

def wc(args):
    """print newline, word, and byte counts for each file"""
    if len(args) < 1:
        usage("Too few arguments", "wc")
        sys.exit(1)
    count = 0
    totallines = 0
    totalwords = 0
    totalcharacters = 0
    for i in args:
        filename = str(i)
        printyes = False
        lines = 0
        words = 0
        characters = 0
        fil = open(i)
        f = []                             # each term in f is each line
        for liness in fil.readlines():
            f.append(liness[0:-1])
        lines += len(f)                     #add to count of lines the amount of lines we looped through
        characters += len(f)
        w = []
        for lin in f:                       #for each line of file
            for x in range(0, len(lin)):    #for each character in line
                if lin[x] == " ":
                    characters += 1         #add to character count for each space
            w += lin.split()                #add this line separated by spaces to w
        words += len(w)                     #add the length of word array to words
        for wrd in w:                       #loop through each word in the word array
            for x in range(0, len(wrd)):
                characters += 1             #count each character in the array
        fil.close()
        count += 1
        if len(args) > 1:
            printyes = True
            totallines += lines
            totalwords += words
            totalcharacters += characters
        print(str(lines) + "\t" + str(words) + "\t" + str(characters) + "\t" + filename)
    if printyes:
        print(str(totallines) + "\t" + str(totalwords) + "\t" + str(totalcharacters) + "\t" + "total")





"""        *WORDCOUNT.PY*
* Send in files and loop through files using a for loop. For each file, create variables lines, words, and characters. Then open
the files using var=open([filename]) and cast those into array f by using
str.split(sep = "\r\n"). Within that array, loop through, counting the number of lines and adding each count to lines and characters.
* Add the contents to another array called l. Loop through w, counting each space and adding that to characters. Then separate by
spaces and send to another array called w.
Loop through that to find number of words and adding it to word. Also in that loop count the characters in each word and add
that to characters.
* Print the name by just saying str = "" + f. That will print the string.
Print a column for lines, words, characters, and the name of the file."""

