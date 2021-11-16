# A list is a collection data type that is ordered, mutable and it allows duplicate elements. Example include:
my_list = ["apple", "banana", "cherry"]
print(my_list)

my_list2 = list
print(my_list2)

my_list2 = [6, False, "Rambutan"]
print(my_list2)
# it can contain to variables together i.e

my_list2 = [6, False, 'Rambutan', "Rambutan"]
print(my_list2)

# to access an object you use index i.e
item = my_list[0]
print(item)

item = my_list[1]
print(item)

item = my_list[2]
print(item)

#it just an example{item = my_list[8]}
#same here {print(item)}

# you can also refer to negative index just use this,
item = my_list[-1]
print(item)

item = my_list[-2]
print(item)

item = my_list[-3]
print(item)

# For iteration use for-in loop, i.e
#for x in my_list:
	#print[X]
	
if "banana" in my_list:
	print("yes")
else:
	print("no")
	
if "cherry" in my_list:
	print("yes")
else:
	print("no")
	
if "apple" in my_list:
	print("yes")
else:
	print("no")
		
if "lemon" in my_list:
	print("yes")
else:
	print("no")
	
if "peach" in my_list:
	print("yes")
else:
	print("no")
	
# To check how many element in a list i.e
print(len(my_list))
print(len(my_list2))
# to append a list
my_list.append("lemon")
print(my_list)
# to insert an element at a position in a list.
my_list.insert(2, "blueberry")
print(my_list)
# to remove an item at a given position in a list.
item = my_list.pop()
print(item)
print(my_list)
# to remove an element from a list.
item = my_list.remove("cherry")
print(my_list)
# to clear all element in a list
item = my_list.clear()
print(my_list)
# to reverse all element in a list
my_list = ["apple", "banana", "cherry"]
my_list.reverse()
print(my_list)
# to sort elements in a list.
my_list.sort()
print(my_list)

mylist =[1,6,8,9,4,0,7,2,3]
mylist.sort()
print (mylist)

new_list = sorted(mylist)
print(new_list)

# some use full trick

mylist = [7]*5
print(mylist)

mylist2 = [4]*7
print(mylist2)
new_list = mylist + mylist2
print(new_list)

# slicing and indexing
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5]
print(a)
b = mylist[:5]
print(b)
c = mylist[1:]
print(c)
d = mylist[1:5]
print(d)
e = mylist[::]
print(e)
f = mylist[::1]
print(f)
g = mylist[::2]
print(g)
h = mylist[::3]
print(h)

# to copy a list
list_org = ["apple", "banana", "cherry"]

list_copy = list_org
print(list_copy)
list_copy.append("lemon")
print(list_copy)
print(list_org)


list_org = ["apple", "banana", "cherry"]

list_copy = list(list_org)
print(list_copy)
list_copy.append("lemon")
print(list_copy)
print(list_org)


list_org = ["apple", "banana", "cherry"]

list_copy = list_org[:]
list_copy.append("lemon")
print(list_copy)
print(list_org)

# another trick 
a = [1,2,3,4,5,6,7,8,9]
b = [i*i for i in a]
print (b)
c = [x*x*x for x in a]
print (c)