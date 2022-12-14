n = int(input())

p_tree = {}

for _ in range(1, n):
    line = input()
    child, parent = line.split()
    p_tree[child] = parent

all_man = set(p_tree.keys()) | set(p_tree.values())

heights = {}

def f(name):
    if name not in p_tree:
        heights[name] = 0
        return 0
    parent = p_tree[name]
    if parent in heights:
        value = heights[parent] + 1
    else:
        value = f(parent) + 1
    heights[name] = value
    return value

for name in all_man:
    if name not in heights:
        f(name)
for name in sorted(heights):
    print(name, heights[name])
