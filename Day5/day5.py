with open('input5.txt') as f:
    lines = f.readlines()

stacks = [
['T','Q','V','C','D','S','N'],
['V','F','M'],
['M','H','N','P','D','W','Q','F'],
['F','T','R','Q','D'],
['B','V','H','Q','N','M','F','R'],
['Q','W','P','N','G','F','C'],
['T','C','L','R','F','W'],
['S','N','Z','T'],
['N','H','Q','R','J','D','S',"M"]
]

moves = []
for line in lines:
    curr = line.split(' ')
    moves.append((int(curr[1]),int(curr[3]),int(curr[5][0:len(curr[5])-1])))

#part 1
for num,source,dest in moves:
    for i in range(num):
        top = stacks[source-1].pop(0)
        stacks[dest-1].insert(0,top)

ans = []
for stack in stacks:
    ans.append(stack[0])
print("".join(ans))

#part 2
stacks = [
['T','Q','V','C','D','S','N'],
['V','F','M'],
['M','H','N','P','D','W','Q','F'],
['F','T','R','Q','D'],
['B','V','H','Q','N','M','F','R'],
['Q','W','P','N','G','F','C'],
['T','C','L','R','F','W'],
['S','N','Z','T'],
['N','H','Q','R','J','D','S',"M"]
]

for num,source,dest in moves:
    top = stacks[source-1][0:num]
    stacks[source-1] = stacks[source-1][num:len(stacks[source-1])]
    stacks[dest-1] = top + stacks[dest-1]

ans = []
for stack in stacks:
    ans.append(stack[0])
print("".join(ans))