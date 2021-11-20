# Tuples are collection data type that are ordered, immutable, it allows element duplicate

tuple1 = type("Tom") # in order to make this a tuple it should be mytupl = type("Tom",)
print(tuple1)


#Creating a tuple from a list
tuple2 = tuple(["apple", "banana", "orange", "blueberry", "cherry", "lemon"])
print(tuple2)


# Acessing elementby indexing
item = tuple2[2]
print(item)
item = tuple2[4]
print(item)
item = tuple2[-2]
print(item)
"""
item = tuple2[7]
print(item)             this gives an error

tuple2[0] = "Jimmy "    this too gives an error
"""


# Iterating over a tuple
for i in tuple2:
    print(i)  # the 'i' could be any alphabet


# Checking is an element is inside a tuple
if "Thomas" in tuple2:
    print("yes")
else:
    print("no")


# Checking the length of a tuple
tuple2 = ("apple", "banana", "orange", "apple", "blueberry", "cherry", "lemon")
print(len(tuple2))
print(tuple2.count("apple"))
print(tuple2.index("apple"))    # it takes the possition of the first element
print(tuple2.index("banana"))


# Convert a datatype from a tuple
my_list = list(tuple2)
print(my_list)
tuple3 = tuple(my_list)
print(tuple3)


# Slicing with a tuple
tuple4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
a = tuple4[5:]
print(a)
b = tuple4[:13]
print(b)
c = tuple4[-10:]
print(c)
c = tuple4[:-6]
print(c)
d = tuple4[2:8]
print(d)
e = tuple4[-1:-10]
print(e)
f = tuple4[1::]
print(f)
g = tuple4[::4]
print(g)
h = tuple4[1::3]
print(h)
h = tuple4[1::3]
print(h)


# Equating Value to element in a tuple
my_tuple = "Tom", 35, "New York"
name, age, city = my_tuple
print(name)
print(age)
print(city)


# Upack multiple element with an "*"
tuple5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
i1, *i2, i3, = tuple5
print(i1)
print(i2)
print(i3)


# Comparism between a tuple and a list data sizes
import sys
my_list = [0, 1, 2, "Hello", True]
my_tuple = [0, 1, 2, "Hello", True]
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")



# Another example
import timeit
print(timeit.timeit(stmt="0, 1, 2, 3, 4, 5", number=100000000))
print(timeit.timeit(stmt="0, 1, 2, 3, 4, 5", number=100000000))
