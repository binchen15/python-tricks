import itertools as it

robots = [{
    'name': 'blaster',
    'faction': 'autobot'
}, {
    'name': 'galvatron',
    'faction': 'decepticon'
}, {
    'name': 'jazz',
    'faction': 'autobot'
}, {
    'name': 'metroplex',
    'faction': 'autobot'
}, {
    'name': 'megatron',
    'faction': 'decepticon'
}, {
    'name': 'starcream',
    'faction': 'decepticon'
}]

print("before sorting, not you expected:")
for key, grouper in it.groupby(robots, key=lambda x: x['faction']):
    print(f"  {key}=>{list(grouper)}")

print("after in-place sorting, you get what you want:")
robots.sort(key=lambda x: x['faction'])
for key, grouper in it.groupby(robots, key=lambda x: x['faction']):
    print(f"  {key}=>{list(grouper)}")


