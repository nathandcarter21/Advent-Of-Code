with open('input4.txt') as f:
    lines = f.readlines()
    
pairs = []
for line in lines:
    i = 0
    num1 = ""
    while line[i] != "-":
        num1 += line[i]
        i+=1
    i+=1
    num2 = ""
    while line[i] != ",":
        num2 += line[i]
        i+=1
    i+=1
    num3 = ""
    while line[i] != "-":
        num3 += line[i]
        i+=1
    i+=1
    num4 = ""
    while line[i] != "\n":
        num4 += line[i]
        i+=1
    pairs.append((int(num1),int(num2),int(num3),int(num4)))

# part 1
ans = 0
for a,b,c,d in pairs:
    if a <= c and b >= d:
        ans += 1
    elif c <= a and d >= b:
        ans += 1
print(ans)

# part 2
ans = 0
for a,b,c,d in pairs:
    if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
        ans += 1
    
print(ans)