"""
Dictionary is a collection data type that is that is unordered and mutable.
It consist of key value pairs which each key value pair maps to it's corresponding value.
"""
# The dictionary general example
mydict = {"name": "Thomas", "age": 25, "city": "New York"}
print(mydict)
print()

 
# Using the dictionary function to create a dictionary.
mydict1 = dict(name = "Tom", age = 28, city = "Lagos")
print(mydict1)
print()


# To access a value in the dictionary
value = mydict1["name"]
print(value)
value1 = mydict1["age"]
print(value1)
value2 = mydict1["city"]
print(value2)
print()


# Addition of values in a dictionary.
mydict["email"] = "tom@web3.py"
print(mydict)
print()


# Deleting in dictionary.
del mydict["name"]
print(mydict)
mydict1.pop("age")
print(mydict1)
mydict1.popitem()
print(mydict1)
print()


# To check whether a value is in a dictionary.
if "name" in mydict1:
    print(mydict1["name"])
    #print(mydict1["lastname"]) \\ it will give an error.
    print()


# Using try-except method to acess a value in a dictionary.
mydict = {"name": "Thomas", "age": 25, "city": "New York"}
print(mydict)
try:
    print(mydict["name"])
except:
    print("ERROR")
try:
    print(mydict["lastname"])
except:
    print("ERROR")
    print()


# Using for-in loop in a dictionary.
for key in mydict:
    print(key)
    print()
for key in mydict.keys():
    print(key)
    print()
for value in mydict.values():
    print(value)
for key, value in mydict.items():
    print(key, value)
print()


# Using dictionary functions.
mydict = {'name': 'Tom', 'age': 28, 'city': 'Lagos'}
mydict_cpy = mydict1
print(mydict_cpy)
mydict_cpy["name"] = "Seun shorty"
print(mydict) # It also affect the original dictionary.
mydict = {"name": "Thomas", "age": 25, "city": "New York"}
mydict_cpy = mydict.copy()
mydict_cpy["name"] = "Seun shorty"
print(mydict_cpy)
print(mydict)
print()


# Using the update function in a dictionary.
mydict = {'name': 'Tom', 'age': 28, "email" : "Shorty@swarty.io"}
mydict2 = {'name': 'John', 'age': 52, 'city': 'London'}
mydict.update(mydict2)
print(mydict)


# Dictionary can be any immutable item i.e tuples, numbers, etc