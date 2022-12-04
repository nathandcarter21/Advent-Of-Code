with open('input3.txt') as f:
    lines = f.readlines()
    
#part 1
ans = 0
for line in lines:
    set1 = set()
    set2 = set()
    for i in range(len(line)//2):
        set1.add(line[i])
    for i in range(len(line)//2, len(line)-1):
        set2.add(line[i])
    intersection = set1.intersection(set2)
    for el in intersection:
        c = el
    if ord(c) >= 97:
        ans += ord(c) - ord('a')+1
    else:
        ans += ord(c) - ord('A') + 27
print(ans)
#part 2
ans = 0
for i in range(0,len(lines),3):
    set1 = set()
    set2 = set()
    set3 = set()
    for j in range(len(lines[i])-1):
        set1.add(lines[i][j])
    for j in range(len(lines[i+1])-1):
        set2.add(lines[i+1][j])
    for j in range(len(lines[i+2])-1):
        set3.add(lines[i+2][j])
    
    intersection = set1.intersection(set2,set3)
    for el in intersection:
        c = el
    if ord(c) >= 97:
        ans += ord(c) - ord('a')+1
    else:
        ans += ord(c) - ord('A') + 27
print(ans)
    
        
    