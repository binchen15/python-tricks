# The ChainMap class manages a sequence of dictionaries, 
# + and searches through them in the order they are given to find values by keys. 
# A ChainMap makes a good “context” container, since it can be treated as a stack for 
# + which changes happen as the stack grows, with these changes being discarded again 
# + as the stack shrinks.

from collections import ChainMap

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = ChainMap(a, b)

print(m.maps)
print('c = {}'.format(m['c']))

# reverse the list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))

# new_child()
m2 = m.new_child()
m2['c'] = "E"
print(m2.maps)

c = {'c': 'E'}
m3 = m.new_child(c)
print(m3.maps)
