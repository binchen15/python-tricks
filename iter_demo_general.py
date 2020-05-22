# ref: https://pymotw.com/

import itertools as it
import operator  as op 

data = [1,2,3,4,5]
result = it.accumulate(data, op.mul)
print(list(result))

data = [1,1,2]
result = it.combinations(data, 2)
print(list(result))


result = it.combinations_with_replacement(data, 2)
print(list(result))

# it.cycle
result = it.cycle([1,-1])

# chain
#it.chain(*iterables)

# it.filterfalse(predicate, iterable)
# return the false ones

# itertools.islice(iterable, start, stop[, step])
# return an iterable, not copy part of array
result = it.islice(range(10), 3)
print(list(result))

# itertools.permutations(iterable, r=None)
result = it.permutations(range(3), 2)
print(list(result))

# product
result = it.product(range(3), 'abc')
print(list(result))

# repeat(object[, ntimes])
result = it.repeat('abc', 3)
print(list(result))

# starmap  op.mul(*[2,6])
data = [(2, 6), (8, 4), (7, 3)]
result = it.starmap(op.mul, data)
for each in result:
    print(each)

# it.takewhile (only 1 cut)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = it.takewhile(lambda x: x<5, data)
for each in result:
    print(each)

# it.dropwhile (only 1 cut)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = it.dropwhile(lambda x: x<5, data)
for each in result:
    print(each)

# itertools.tee(iterable, n=2)
# return n independent iterators for iterable given
colors = ['red', 'orange', 'yellow', 'green', 'blue']
alpha_colors, beta_colors = it.tee(colors)
for each in alpha_colors:
    print(each)
print('..')
for each in beta_colors:
     print(each)

# it.zip_longest(*iterables, fillvalue=None)
colors = ['red', 'orange', 'yellow', 'green', 'blue',]
data   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
for each in it.zip_longest(colors, data, fillvalue=None):
    print(each)

