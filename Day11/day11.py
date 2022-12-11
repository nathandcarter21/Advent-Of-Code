from heapq import heappop, heappush


with open('input11.txt') as f:
    lines = f.readlines()

monkeys = [] 

class Monkey:
    def __init__(self,items,test,t,f):
        self.items = items
        self.test = test
        self.t = t
        self.f = f
        self.i = 0

for i in range(8):
    monkey = lines[0+(i*7)].split()
    items = lines[1+(i*7)].split()
    test = lines[3+(i*7)].split()
    test = int(test[3])
    t = lines[4+(i*7)].split()
    t = int(t[5])
    f = lines[5+(i*7)].split()
    f = int(f[5])
    curr = []
    for i in range(2,len(items)):
        if items[i][-1] == ',':
            curr.append(int(items[i][0:len(items[i])-1]))
        else:
            curr.append(int(items[i]))
    mon = Monkey(curr,test,t,f)
    monkeys.append(mon)

for i in range(20):
    for i in range(len(monkeys)):
        while monkeys[i].items:
            item = monkeys[i].items.pop(0)
            monkeys[i].i += 1
            new = 0
            if i == 0:
                new = item * 11
            elif i == 1:
                new = item + 8
            elif i == 2:
                new = item * 3
            elif i == 3:
                new = item + 4
            elif i == 4:
                new = item * item
            elif i == 5:
                new = item + 2
            elif i == 6:
                new = item + 3
            elif i == 7:
                new = item + 5
            new = new//3
            if new % monkeys[i].test == 0:
                monkeys[monkeys[i].t].items.append(new)
            else:
                monkeys[monkeys[i].f].items.append(new)
heap = []
for monkey in monkeys:
    heappush(heap,monkey.i*-1)
ans = 1
for i in range(2):
    ans *= heappop(heap) * -1
print(ans)

# part 2
monkeys=[]
for i in range(8):
    monkey = lines[0+(i*7)].split()
    items = lines[1+(i*7)].split()
    test = lines[3+(i*7)].split()
    test = int(test[3])
    t = lines[4+(i*7)].split()
    t = int(t[5])
    f = lines[5+(i*7)].split()
    f = int(f[5])
    curr = []
    for i in range(2,len(items)):
        if items[i][-1] == ',':
            curr.append(int(items[i][0:len(items[i])-1]))
        else:
            curr.append(int(items[i]))
    mon = Monkey(curr,test,t,f)
    monkeys.append(mon)

mod = 1
for monkey in monkeys:
    mod *= monkey.test
for i in range(10000):
    for i in range(len(monkeys)):
        while monkeys[i].items:
            item = monkeys[i].items.pop(0)
            monkeys[i].i += 1
            new = 0
            if i == 0:
                new = item * 11
            elif i == 1:
                new = item + 8
            elif i == 2:
                new = item * 3
            elif i == 3:
                new = item + 4
            elif i == 4:
                new = item * item
            elif i == 5:
                new = item + 2
            elif i == 6:
                new = item + 3
            elif i == 7:
                new = item + 5
            new = new % mod
            if new % monkeys[i].test == 0:
                monkeys[monkeys[i].t].items.append(new)
            else:
                monkeys[monkeys[i].f].items.append(new)
heap = []
for monkey in monkeys:
    heappush(heap,monkey.i*-1)
ans = 1
for i in range(2):
    ans *= heappop(heap) * -1
print(ans)