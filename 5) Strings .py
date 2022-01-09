# A string is a collectin data type that is ordered and immutable. It is the text representation in python.
string = 'hello world'
print(string)
string1 = 'I a\'m a programmer' # you can use this ("") or add (\) thisat the appropraite space.
print(string1)
string2 = """hello
world
this multiple line of string in python"""
print(string2)
print()


# Getting a value of a string
string3 = "hello world"
print(string3[0])
print(string3[1])
print(string3[-1])
print(string3[-4])
print()


# Slicing a string
print(string3[:])
print(string3[2:])
print(string3[:7])
print(string3[-3:])
print(string3[:-5])
print(string3[2:6])
print(string3[-2:-7])
print(string3[2::-7])
# A string deosn't allow you to change it's values.
print()


# How to cattenate
greeting = "Hello"
name = "George Floyd"
TheSentence = greeting + " " + name
print(TheSentence)
print()


# For in loop in a string
greeting = "hello"
for i in greeting:
    print(i)
print()


# How to check for a value in a string
greeting = "Hello"
if 'l' in greeting:
    print("yes")
else:
    print("no")
print()


# other string function
myString = "     Baka yaro     "
print(myString)
myString = myString.strip()
print(myString)
print(myString.upper())
print(myString.lower())
print(myString.startswith("yaro"))
print(myString.startswith("World"))
print(myString.endswith("Hello"))
print(myString.endswith("World"))
print(myString.find("llo"))
print(myString.find("p"))
print(myString.count("l"))
print(myString.count("P"))
print(myString.replace("world", "Universe")) # This will create a new set.
print(myString.replace("Worlld", "universe"))
print()
 

# List and string in python
myString = "how are you doing"
myList = myString.split()  # to convert from a string to a list 
print(myList)
myList = myString.split(" ")
print(myList)
myString = "how,are,you,doing"
myList = myString.split(" ")
print(myList)
myList = myString.split(",")
print(myList)
newString = "".join(myList) # to convert from a list to a string back
print(newString)
newString = " ".join(myList)
print(newString)
print()


# Other thing related to a string.
myList = ["a"] * 6
print(myList)
myString = "".join(myList)
print(myString)
print()
# Checking how fast a string can run
from timeit import default_timer as timer
myList = ["a"] * 1000000
print(myList)
print()
start = timer()
myString = "".join(myList)
stop = timer()
print(myString)
print(stop-start)
print()


# Formatting a string
var = "thomas"
myString = "the variables is %s" % var
print(myString)
var = 3
myString = "the variables is %s" % var
print(myString)
var = 3.1421486289648554855
myString = "the variables is %f" % var
print(myString)
var = 3.142544854767915415105
myString = "the variables is %.10f" % var # this will specify the amount of special decimals needed.
print(myString)
var = "james"
myString = "the variables is {}".format(var)
print(myString)
var1 = 3.1425597485
var2 = 5
myString = "the variables are {:.5f} and {}".format(var1, var2)
print(myString)
var = "thomas"
myString = f"the variables is {var}" # THis id the fastest and easier method to do it.
print(myString)