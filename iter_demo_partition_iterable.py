# partition an iterable into another iterable of chunks of size n
# ref https://realpython.com/python-itertools/#what-is-itertools-and-why-should-you-use-it

def better_grouper(inputs, n):
    # same references in the following
    iters = [iter(inputs)] * n 
    return zip(*iters)

for _ in better_grouper(range(100000000), 10):
    pass


