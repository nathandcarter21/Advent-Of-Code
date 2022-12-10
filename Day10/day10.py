with open('input10.txt') as f:
    lines = f.read()
lines = lines.split()
# part 1
cycle = 1
reg = 1
ans = 0
nums = set([20,60,100,140,180,220])

data = [0] * 241

for el in lines:
    if el == 'noop':
        data[cycle] = reg
        cycle += 1
    elif el == 'addx':
        data[cycle] = reg
        cycle += 1
    else:
        data[cycle] = reg
        cycle += 1
        reg += int(el)
    if cycle in nums:
        ans += reg * cycle
print(ans)

# part 2

screen = []
position = 1
for r in range(6):
    curr = []
    for c in range(40):
        if abs(data[position] - c) <= 1:
            curr.append('#')
        else:
            curr.append('.')
        position += 1
    screen.append(curr)

for row in screen:
    print("".join(row))
