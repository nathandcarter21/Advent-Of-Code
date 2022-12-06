with open('input6.txt') as f:
    input = f.read()

#part 1
counts = [0] * 26
for i in range(3):
    counts[ord(input[i])-ord('a')]+=1
ans = -1
for i in range(3,len(input)):
    counts[ord(input[i])-ord('a')] += 1
    valid = True
    for num in counts:
        if num > 1:
            valid = False
    if valid:
        ans = i + 1
        break
    counts[ord(input[i-3])-ord('a')] -= 1
print(ans)

#part 2
counts = [0] * 26
for i in range(13):
    counts[ord(input[i])-ord('a')]+=1
ans = -1
for i in range(13,len(input)):
    counts[ord(input[i])-ord('a')] += 1
    valid = True
    for num in counts:
        if num > 1:
            valid = False
    if valid:
        ans = i + 1
        break
    counts[ord(input[i-13])-ord('a')] -= 1
print(ans)