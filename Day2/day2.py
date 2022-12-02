with open('input2.txt') as f:
    lines = f.readlines()
    
ans = 0
#part 1
for line in lines:
    if line[2] == 'X':
        ans += 1
        if line[0] == 'A':
            ans += 3
        elif line[0] == 'B':
            ans += 0
        elif line[0] == 'C':
            ans += 6
    elif line[2] == 'Y':
        ans += 2
        if line[0] == 'A':
            ans += 6
        elif line[0] == 'B':
            ans += 3
        elif line[0] == 'C':
            ans += 0
    elif line[2] == 'Z':
        ans += 3
        if line[0] == 'A':
            ans += 0
        elif line[0] == 'B':
            ans += 6
        elif line[0] == 'C':
            ans += 3
print(ans)
#part 2
ans = 0
for line in lines:
    if line[0] == 'A':
        if line[2] == 'X':
            ans += 3
        elif line[2] == 'Y':
            ans += 1
            ans += 3
        elif line[2] == 'Z':
            ans += 2
            ans += 6
    elif line[0] == 'B':
        if line[2] == 'X':
            ans += 1
        elif line[2] == 'Y':
            ans += 2
            ans += 3
        elif line[2] == 'Z':
            ans += 3
            ans += 6
    elif line[0] == 'C':
        if line[2] == 'X':
            ans += 2
        elif line[2] == 'Y':
            ans += 3
            ans += 3
        elif line[2] == 'Z':
            ans += 1
            ans += 6
print(ans)