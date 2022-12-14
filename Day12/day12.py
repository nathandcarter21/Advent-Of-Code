with open('input12.txt') as f:
    lines = f.readlines()

grid = []
for line in lines:
    curr = []
    for i in range(len(line)-1):
        if line[i] == 'E':
            end = (len(grid),i)
            curr.append(ord('z')-ord('a'))
        elif line[i] == 'S':
            start = (len(grid),i)
            curr.append(ord('a')-ord('a'))
        else:
            curr.append(ord(line[i])-ord('a'))
    grid.append(curr)

def bfs(i, j):
    q = []
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    q.append((0,i,j))
    while len(q) > 0:
        d,i,j = q.pop(0)
        if visited[i][j]:
            continue
        visited[i][j] = True
        if i == end[0] and j == end[1]:
            return d
        for a in range(4):
            newR = i + dir[a][0]
            newC = j + dir[a][1]
            if (0 <= newR < len(grid)) and (0 <= newC < len(grid[0])) and grid[newR][newC] <= grid[i][j] + 1:
                q.append((d+1,newR,newC))

def bfs2(i, j):
    q = []
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    q.append((0,i,j))
    while len(q) > 0:
        d,i,j = q.pop(0)
        if visited[i][j]:
            continue
        visited[i][j] = True
        if grid[i][j] == 0:
            return d
        for a in range(4):
            newR = i + dir[a][0]
            newC = j + dir[a][1]
            if (0 <= newR < len(grid)) and (0 <= newC < len(grid[0])) and grid[newR][newC]+1 >= grid[i][j]:
                q.append((d+1,newR,newC))

# part 1
print(bfs(start[0],start[1]))

# part 2
print(bfs2(end[0],end[1]))