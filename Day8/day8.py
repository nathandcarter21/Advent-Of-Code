with open('input8.txt') as f:
    lines = f.readlines()

grid = []
for line in lines:
    curr = []
    for i in range(len(line)-1):
        curr.append(int(line[i]))
    grid.append(curr)

def n(r,c,val):
    if grid[r][c] >= val:
        return False
    if r == 0:
        return True
    return n(r-1,c,val)

def s(r,c,val):
    if grid[r][c] >= val:
        return False
    if r == len(grid)-1:
        return True
    return s(r+1,c,val)

def e(r,c,val):
    if grid[r][c] >= val:
        return False
    if c == 0:
        return True
    return e(r,c-1,val)

def w(r,c,val):
    if grid[r][c] >= val:
        return False
    if c == len(grid[0])-1:
        return True
    return w(r,c+1,val)

#part 1
ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if r == 0 or c == 0 or r == len(grid)-1 or c == len(grid[0])-1:
            ans += 1
        else:
            if n(r-1,c,grid[r][c]) or s(r+1,c,grid[r][c]) or e(r,c-1,grid[r][c]) or w(r,c+1,grid[r][c]):
                ans += 1
print(ans)

def n2(r,c,val):
    if r <= 0 or grid[r][c] >= val:
        return 1
    return 1 + n2(r-1,c,val)

def s2(r,c,val):
    if r >= len(grid) -1 or grid[r][c] >= val:
        return 1
    return 1 + s2(r+1,c,val)

def e2(r,c,val):
    if c <= 0 or grid[r][c] >= val:
        return 1
    return 1 + e2(r,c-1,val)

def w2(r,c,val):
    if c >= len(grid[0])-1 or grid[r][c] >= val:
        return 1
    return 1 + w2(r,c+1,val)

#part 2
ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        ans = max(ans,(n2(r-1,c,grid[r][c]) * s2(r+1,c,grid[r][c]) * e2(r,c-1,grid[r][c]) * w2(r,c+1,grid[r][c])))
print(ans)

