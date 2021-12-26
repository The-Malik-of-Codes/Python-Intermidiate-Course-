# A set is a collectin data type that is unordered and mutable. It doesn't allow duplicate of values/ element.
from typing import Union


myset = {1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1}
print(myset) # it doesn't allow duplicate of values/ elements.
print()


# Using the set method to create a set of values
myset1 = set([1, 2, 3, 4, 5, 6, 9])
myset2 = set("hello")
print(myset1)
print(myset2)
print()


# Checking whether if a collection of elements are a set or not.
myset3 = {}
print(type(myset3))
myset4 = set()
print(type(myset4))
print()


# Adding some new variales to a set.
myset5 = set()
myset5.add(1)
myset5.add(2)
myset5.add(3)
myset5.add(4)
myset5.add(5)
myset5.add(6)
print(myset5)
print()


# Some set functions
myset5.remove(3)
print(myset5)
myset5.discard(2)
print(myset5)
myset5.discard(8)
print(myset5)
myset5.clear()
myset.pop()
print()


# Using if statement to check for a value in a set and interating a set.
myset6 = set()
myset6.add(10)
myset6.add(20)
myset6.add(30)
myset6.add(40)
myset6.add(50)
myset6.add(60)
myset6.add(70)
print(myset6)
for i in myset6:
    print(i)
if 10 in myset6:
    print("Yes")
print()


# Other set functions
odds = {1, 3, 5, 7, 9, 11, 13}
evens = {0, 2, 4, 6, 8, 10, 12}
primes = {2, 3, 5, 7, 11, 13, 17}
u = odds.union(evens)
print(u)
i = odds.intersection(evens)
print(i)
i2 = odds.intersection(primes)
print(i2)


# Difference of two set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.difference(setB)
print(diff)
diff2 = setB.difference(setA)
print(diff2)
diff3 = setA.symmetric_difference(setA)
print(diff3)
diff4 = setB.symmetric_difference(setA)
print(diff4)


# How to modify a set
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {1, 2, 3, 10, 11, 12, 13, 14, 15}
set1.update(set2)
print(set1)
set1.intersection_update(set2)
print(set1)
set1.difference_update(set2)
print(set1)
set1.symmetric_difference_update(set2)
print(set1)


# Super set and disjoint methods
setA = {1, 2, 3, 4, 5, 6, 7}
setB = {1, 2, 3, 4}
setC = {8, 9, 10}
print(setA.issubset(setB))
print(setB.issubset(setA))
print(setA.issuperset(setB))
print(setB.issuperset(setA))
print(setB.isdisjoint(setA))
print(setB.isdisjoint(setC))


# Copying some values in a set.
setA = {1, 2, 3, 4, 5, 6 ,7, 8, 9}
setB = setA
setB.add(10)
print(setA)
print(setB)
setC = set(setA)
setB.add(10)
print(setA)
print(setC)


# Frozeen set
a = frozenset([1, 2, 3, 4, 5, 6])
# a.add(2) this wont work because the set vale is fixed
# a.remove(2) this wont work because the set vale is fixed
print(a)
