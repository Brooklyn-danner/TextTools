from Usage import usage

def sort(args):
    """sort lines of text files"""
    if len(args) < 1:
        usage("Too few arguments", "sort")

    arr = []
    for i in args:
        f = open(i)
        for lines in f.readlines():
            arr.append(lines[0:-1])
    arr.sort()
    for x in arr:
        print(x)







"""* Begin with funtion def sort(args). Iterate through args using a for loop and add each content into an array.
For each value in this array, load the contents into another array named contents. We will use this single array, contents, as a
holder for the contents in all the inputted files. Call python's sort function on contents. (arr.sort()). From there, loop
through array, printing out each value.
"""

# Your program must use `usage()` to raise an error when too few arguments are given; at a
# minimum the name of one input file is required

#Reverse-sorted data can be obtained by first sorting in order with the `sort`
#tool, then reversing the result with `tac`:
#$ python src/tt.py sort data/colors8 > sortedColors8















""" Correct output:

 $ python src/tt.py sort data/colors8
    Antique White
    Dark Goldenrod
    DarkSea Green
    Dodger Blue
    Favorite Color
    Light Salmon
    Midnight Blue
    Royal Blue
    Snow
    
     $ python src/tt.py sort data/complexity



                    one way is to make it so simple
                that there are no obvious deficiencies."
               and the other is to make it so complicated
               that there are obviously no deficiencies,
         "There are two ways of constructing a software design:
        -- Tony Hoare


 $ python src/tt.py sort data/colors8 data/names10
    Alexa
    Angela
    Antique White
    Bailey
    Dark Goldenrod
    DarkSea Green
    Dodger Blue
    Favorite Color
    Frank
    Hazel
    Isabel
    Jerry
    Kai
    Karen
    Light Salmon
    Midnight Blue
    Mikayla
    Royal Blue
    Snow


$ python src/tt.py sort data/complexity data/debugging





                      how will you ever debug it?"
                    one way is to make it so simple
                as writing a program in the first place.
                that there are no obvious deficiencies."
               and the other is to make it so complicated
               that there are obviously no deficiencies,
            "Everyone knows that debugging is twice as hard
         "There are two ways of constructing a software design:
        -- Brian Kernighan
        -- Tony Hoare
        So if you're as clever as you can be when you write it,



 $ python src/tt.py sort data/names10 data/colors8
    Alexa
    Angela
    Antique White
    Bailey
    Dark Goldenrod
    DarkSea Green
    Dodger Blue
    Favorite Color
    Frank
    Hazel
    Isabel
    Jerry
    Kai
    Karen
    Light Salmon
    Midnight Blue
    Mikayla
    Royal Blue
    Snow
    
      $ python src/tt.py sort data/debugging data/complexity





                      how will you ever debug it?"
                    one way is to make it so simple
                as writing a program in the first place.
                that there are no obvious deficiencies."
               and the other is to make it so complicated
               that there are obviously no deficiencies,
            "Everyone knows that debugging is twice as hard
         "There are two ways of constructing a software design:
        -- Brian Kernighan
        -- Tony Hoare
        So if you're as clever as you can be when you write it,



 $ python src/tt.py sort data/random20
    1
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    2
    20
    3
    4
    5
    6
    7
    8
    9
    
    
 $ python src/tt.py sort data/colors8 > sortedColors8

    $ python src/tt.py tac sortedColors8
    Snow
    Royal Blue
    Midnight Blue
    Light Salmon
    Favorite Color
    Dodger Blue
    DarkSea Green
    Dark Goldenrod
    Antique White

"""
