from collections import Counter

c = Counter("Hello World!")
print(c)

s = 'the lazy dog jumped over another lazy dog'    
c = Counter(s.split(" ")) 
print(c.most_common(3))
print(c.most_common()) 

c = Counter(a=3,b=5,e=2) 
print(c.most_common()) 

c = Counter({"a":3, "b":4, "e":2})  
print(c.most_common())   
c.elements() 
# <itertools.chain at 0x10e6ac860>

c = Counter(dict([("a",3),("b",4),("e",2)]))   # convert from a list of(elem, cnt) 
print(c)


sum(c.values())                 # total of all counts 
list(c)                         # list unique elements 
set(c)                          # convert to a set 
dict(c)                         # convert to a regular dictionary 
c.items()                       # convert to a list like (elem, cnt) 
c.clear()                       # reset all counts 

c = Counter({"a":3, "b":4, "e":2, "f":-2})
c += Counter()                  # remove zero and negative counts
print(c)



