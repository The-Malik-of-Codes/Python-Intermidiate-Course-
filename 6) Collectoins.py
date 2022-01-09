# A collection is a counter, namedtuple, an ordereddict, a defualtdict, deque

# From a counter aspect
from collections import Counter
z = "aaaaaaaabbbcccccc"
myCounter = Counter(z)
print(myCounter)
print(myCounter.items())
print(myCounter.keys())
print(myCounter.values())
print(myCounter.most_common(1))
print(myCounter.most_common(2))
print(myCounter.most_common(1)[0][0])
print(list(myCounter.elements()))
print()


# From a namedtuple aspect
from collections import namedtuple
point = namedtuple("point", "x, y")
pt = point(1, -4)
print(pt)
print(pt.y, pt.y)
print()


# From an ordered dict
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["e"] = 5
ordered_dict["f"] = 6
print(ordered_dict)
print()


# From a defualt dict
from collections import defaultdict
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
dict = defaultdict(float)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])


# From a function called deque
from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.extend([4, 5, 6])
print(d)
d.clear()
print(d)
