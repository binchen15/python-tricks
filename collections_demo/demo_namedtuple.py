from collections import namedtuple

# subclass tuple
# Namedtuples are also a memory-efficient option when defining an immutable 
# +class in Python.

fruit = namedtuple('fruit', ['name',  'color', 'price'])
watermelon = fruit('watermelon', 'green', 1.00)
print(watermelon)
print(watermelon.color, watermelon.name, watermelon.price)
print(watermelon._asdict())
