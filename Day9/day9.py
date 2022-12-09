with open('input9.txt') as f:
    lines = f.readlines()

def moveTail():
    distX = head[0]-tail[0]
    distY = head[1]-tail[1]
    if abs(head[0] - tail[0]) > 1 or abs(head[1]-tail[1]) > 1:    
        if head[1] == tail[1] and head[0] - tail[0] > 1:
            tail[0] += 1
        elif head[1] == tail[1] and head[0] - tail[0] < -1:
            tail[0] -= 1
        elif head[0] == tail[0] and head[1] - tail[1] > 1:
            tail[1] += 1
        elif head[0] == tail[0] and head[1] - tail[1] < -1:
            tail[1] -= 1

        elif head[0] > tail[0] and head[1] > tail[1]:
            tail[0] += 1
            tail[1] += 1
        elif head[0] > tail[0] and head[1] < tail[1]:
            tail[0] += 1
            tail[1] -= 1
        elif head[0] < tail[0] and head[1] > tail[1]:
            tail[0] -= 1
            tail[1] += 1
        elif head[0] < tail[0] and head[1] < tail[1]:
            tail[0] -= 1
            tail[1] -= 1
        
        visited.add((tail[0],tail[1]))

# part 1
visited = set()
visited.add((0,0))

head = [0,0]
tail = [0,0]

for line in lines:
    line = line.split()
    count = int(line[1])
    for i in range(count):
        if line[0] == "R":
            head[0] += 1
            moveTail()
        elif line[0] == "L":
            head[0] -= 1
            moveTail()
        elif line[0] == "U":
            head[1] += 1
            moveTail()
        elif line[0] == "D":
            head[1] -= 1
            moveTail()
print(len(visited))

#part 2

def moveNode(tail,head):
    if tail > 9: return
    distX = nodes[head][0]-nodes[tail][0]
    distY = nodes[head][1]-nodes[tail][1]
    if abs(nodes[head][0] - nodes[tail][0]) > 1 or abs(nodes[head][1]-nodes[tail][1]) > 1:    
        if nodes[head][1] == nodes[tail][1] and nodes[head][0] - nodes[tail][0] > 1:
            nodes[tail][0] += 1
        elif nodes[head][1] == nodes[tail][1] and nodes[head][0] - nodes[tail][0] < -1:
            nodes[tail][0] -= 1
        elif nodes[head][0] == nodes[tail][0] and nodes[head][1] - nodes[tail][1] > 1:
            nodes[tail][1] += 1
        elif nodes[head][0] == nodes[tail][0] and nodes[head][1] - nodes[tail][1] < -1:
            nodes[tail][1] -= 1

        elif nodes[head][0] > nodes[tail][0] and nodes[head][1] > nodes[tail][1]:
            nodes[tail][0] += 1
            nodes[tail][1] += 1
        elif nodes[head][0] > nodes[tail][0] and nodes[head][1] < nodes[tail][1]:
            nodes[tail][0] += 1
            nodes[tail][1] -= 1
        elif nodes[head][0] < nodes[tail][0] and nodes[head][1] > nodes[tail][1]:
            nodes[tail][0] -= 1
            nodes[tail][1] += 1
        elif nodes[head][0] < nodes[tail][0] and nodes[head][1] < nodes[tail][1]:
            nodes[tail][0] -= 1
            nodes[tail][1] -= 1
        
        moveNode(tail+1,tail)

visited.clear()
visited.add((0,0))
nodes = [[0,0] for i in range(10)]
for line in lines:
    line = line.split()
    count = int(line[1])
    for i in range(count):
        if line[0] == "R":
            nodes[0][0] += 1
            moveNode(1,0)
        elif line[0] == "L":
            nodes[0][0] -= 1
            moveNode(1,0)
        elif line[0] == "U":
            nodes[0][1] += 1
            moveNode(1,0)
        elif line[0] == "D":
            nodes[0][1] -= 1
            moveNode(1,0)
        visited.add((nodes[9][0],nodes[9][1]))
print(len(visited))