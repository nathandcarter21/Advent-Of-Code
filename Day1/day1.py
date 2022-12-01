from heapq import heappop, heappush

with open('input1.txt') as f:
    lines = f.readlines()
curr = 0
heap = []

for i in range(len(lines)):
    if lines[i] == '\n':
        heappush(heap,curr * -1)
        curr = 0
    else:
        curr += int(lines[i])
print(heap[0]*-1)

ans = 0
for i in range(3):
    ans += heappop(heap) * -1
print(ans)