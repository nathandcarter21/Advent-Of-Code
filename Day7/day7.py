from heapq import heapify, heappop

with open('input7.txt') as f:
    lines = f.readlines()

class Dir:
    def __init__(self,parent=None,name="defaultName"):
        self.parent = parent
        self.name = name
        self.size = 0
        self.subdir = {}

root = None
curr = None
for line in lines:
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                newDir = Dir(None, line[2])
                curr = newDir
                root = newDir
            elif line[2] == '..':
                curr = curr.parent
            else:
                curr = curr.subdir[line[2]]
    elif line[0] == 'dir':
        newDir = Dir(curr,line[1])
        curr.subdir[line[1]] = newDir
    else:
        curr.size += int(line[0])


def getSum(node):
    total = node.size
    for name, d in node.subdir.items():
        total += getSum(d)
    return total

def rec(node):
    s = getSum(node)
    if s <= 100000:
        ans.append(s)
    allDir.append(s)
    for name, d in node.subdir.items():
        rec(d)

#part 1
ans = []
allDir = []
rec(root)
print(sum(ans))

#part 2
ans = -1
needToFree = 30000000-(70000000 - getSum(root))
heapify(allDir)
while allDir:
    num = heappop(allDir)
    if num >= needToFree:
        ans = num
        break
print(ans)