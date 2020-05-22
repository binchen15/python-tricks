from collections import OrderedDict
#dict subclass that remembers the order in which that keys were first inserted.

# order is not sort.
# it can be used in conjunction with sorting to make a sorted dictionary

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

print("order by name")
od = OrderedDict(sorted(d.items(), key=lambda x : x[0]))
print(od)

print('order by values')
od = OrderedDict(sorted(d.items(), key=lambda x : x[1]))
print(od)

