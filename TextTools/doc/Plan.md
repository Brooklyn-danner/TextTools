# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

*   A detailed written description of the problem this program aims to solve.
*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
In this assignment I am manually creating my own versions of popular Unix text-processing programs. The programs I am to mimick are
cat, tac, cut, paste, grep, head, tail, sort, and wc.

Program		|	Description
----------------|----------------------
cat		|	take in a given list of files and print them all out
tac		|	take in a given list of files and print them all out backwards
paste		|	take in a given list of files and print all line ones together on the first line, each separated by commas,
. 		|	all line twos together on line two, spearated by commas, etc
cut		|	Print out the first column of a CSV file unless otherwise specified. Then print out that file.
grep		|	Take in a string and a list of files. Search the file for that string and print all the lines of the files
. 		|	that contain that string. If "-v" is in front of the inputted string, then search for all the lines that
. 		|	DONT have that string in it.
head		|	Functions the same as cat except it prints the first 10 lines of the file. If the function is called with
.		|	with the "-n" argument followed by a number, n, print the nth number of lines
tail		|	Tail functions the same as head, except it prints the last 10 lines of the file. Likewise, if the function
.		|	is called with the "-n" argument and number, n, then print the last nth number of lines
sort		|	This prints the inputted file into lexical order (sorted by ASCII value). If multiple files are given, mix
.		|	mix them together as if it was one and sort them.
wc		|	Prints the number of lines, words, and characters, and name of all files. Words are separated by whitespace
.		|	and lines are determined by \r\n.

## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).
---------------------------------------------------------------------------------------------
All of the programs will take in one or more files, meaning it must use open() to take in the contents of the file and read
the string. It will use tt.py as a runner to on these files by calling "python src/tt.py [program name] [file] [file]" etc.
Each call will output a string that is a modification of the inputted files. In each program, loop through the lines in the
file by using f.readLines(). For each line do the required modification. 


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.
	*CONCATENATE.PY*
* Have a method called cat and a method called tac. 
* In cat, open the file and then do a for loop. Use "For lines in var.readlines()" and then 
print out lines. This will output in a string. 
* In tac, open the file, create an empty string, then do a for loop (the same as above). Inside the loop: empty
string = lines + empty string. This will print it out backwards. In both methods, in the case that you cannot open the file, the
open() function automagically throws an error so my code will not blow up (yayy!!)
	*CUTPASTE.PY*
* Have a method called cut and a method called paste. 
*	In paste, open all files and set them to different variable names. Find the 
file with the largest number of lines. Use that as the count for the loop. (for x in range [largest number of lines])
Within the loop print out the specific line in each file (variable.readline()). Readline also prints out an extra
line after that so make sure you account for that
*	In cut, read each line of the CSV file as a string and call .split on it using a comma as the separator. This will 
give us the desired strings or empty strings in the place of each file. Print out the 0th value in the array if "-f" isn't 
called. If it is, split the inputted numbers into an array separated by commas as well. Loop through array finding the smallest
fth number and printing out that f-1th value of the array. Remove that value from array and repeat. Put all of it in a while len
is greater than 0 loop so no errors are thrown. 
	*GREP.PY*
* First check to see if "-v" is used when calling grep. 
If not:
*	Loop through each file by using readlines() function. In that loop, read the string that accompanies each readlines
iteration by using if s in str boolean call. If that line contains it, print it out.
If yes:
*	Do the same thing as above, except if s in str = false then print out the string.
	*PARTIAL.PY* 
* Two methods:
* 	Head- Check to see if -n was called with the function. Then check to see if there was more than one inputted file. If there 
was, then print out the banner that says the name of the file; if not, don't worry about it.
If -n was not called, use a "for x in range 10" loop to iterate. In 
each iteration print .readline() but be careful about the
extra line at the end when readline is called. If -n was called, simply switch to using for x in range n.
*	Tail- Read in the file using open() and load it into an array. Use str.split(sep = "\n"). Then, loop through the array backwards 10 
times. If "-v" is called, print content of array v times.
* Take into consideration if v is longer than contents of file. Call usage if so.
	*SORTING.PY*
* Begin with funtion def sort(args). Iterate through args using a for loop and add each content into an array.
For each value in this array, load the contents into another array named contents. We will use this single array, contents, as a
holder for the contents in all the inputted files. Call python's sort function on contents. (arr.sort()). From there, loop 
through array, printing out each value.
	*WORDCOUNT.PY*
* Send in files and loop through files using a for loop. For each file, create variables lines, words, and characters. Then open
the files using var=open([filename]) and cast those into array f by using 
str.split(sep = "\r/n"). Within that array, loop through, counting the number of lines and adding each count to lines and characters.
* Add the contents to another array called l. Loop through w, counting each space and adding that to characters. Then separate by 
spaces and send to another array called w. 
Loop through that to find number of words and adding it to word. Also in that loop count the characters in each word and add
that to characters. 
* Print the name by just saying str = "" + f. That will print the string.
Print a column for lines, words, characters, and the name of the file.

## Phase 3: Implementation *(15%)*

**Deliver:**
*   I struggled a lot with extra lines being printed when I didn't want them to be. I ran into this almost every implemenation 
in the beggining, but by the end I was able be proactive and cut off the extra line before I completed my code.
*   I found that my plan for cut was way off. I didn't need to modify the array at all. I just needed to call the sort function and
then it would automagically print out what I needed in order
*   On the other hand, my plan for word count was spot on. I followed exactly what my pseudocode said and it worked perfectly.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

* I ran my code against all of the test cases posted in the examples. 
* Bugs found:
*	I accidentally put two wc ifs in tt.py without realizing it, so my program would run twice everytime I called it. It took
me so long to figure out because I put that if in tt.py before I even began coding the problem so it wasn't in the area I recently
was typing in. Also in wc I put the same variable name twice for two different things so I couldn't figure out why it was giving me
the wrong output. I also put the total values inside of the for loop so they reset for every file. It would print out the numbers
for the last file called, not the total values.
*	In partial.py, when I called the for in range loop I forgot that the last number was exclusive so it didn't iterate as many
times as I needed it to. I also realized I needed to cast n as an int because we read it in as a string
*	In tail, my indentation was messed up so it all fell into one if statement causing a lot of my tests to not even run
*	In append I ran into the problem of printing too many lines in between contents


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
Those with a lot of nested for loops.
        *   Are there parts of your program which you aren't quite sure how/why they work?
No. I made sure I only used syntax that I could understand and I came up with.
        *   If a bug is reported in a few months, how long would it take you to find the cause?
It would depend on the file. Some of the files I did a very good job commenting. Others, there is no commenting at all.
    *   Will your documentation make sense to
        *   anybody besides yourself?
Yes. I only used basic syntax to get the job done; nothing too fancy
        *   yourself in six month's time?
Yes. Once again, it is very basic code
    *   How easy will it be to add a new feature to this program in a year?
It wouldn't be hard, but if I had programmed with that in the back of my mind I would've done a few things a little differently.
    *   Will your program continue to work after upgrading
        *   your computer's hardware?
Yes.
        *   the operating system?
Yes.
        *   to the next version of Python?
I think so. Because I used only syntax that is basically the backbone of Python. It should work for years and years and years
down the road.
