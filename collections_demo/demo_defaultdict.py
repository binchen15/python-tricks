from collections import defaultdict

# first argument must be callable or None
wc = defaultdict(int)
print(wc['hello'])

dd = defaultdict(list)
print(dd)
dd['a'].append("Hello")
dd['a'].append("World")
print(dd)
