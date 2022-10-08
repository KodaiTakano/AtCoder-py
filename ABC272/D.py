from dis import dis
import math
from queue import Queue

N, M = map(int, input().split())
dist=[[-1]*N for _ in range(N)]
xy=[]
for i in range(1,401):
    for j in range(1,401):
        if i**2+j**2==M:
            xy.append([i, j])
que = Queue()
print(dist)
dist[0][0] = 0
print(dist)
que.put([0, 0])

while not que.empty():
    v = que.get()
    
    for i, j in xy:
        next_v = [[v[0]+i, v[1]+j], [v[0]+i, v[1]-j], [v[0]-i, v[1]+j], [v[0]-i, v[1]-j]]
        print(i, j)
        for n in range(4):
            if 0<=next_v[n][0]<N and 0<=next_v[n][1]<N:
                if dist[next_v[n][0]][next_v[n][1]] < dist[v[0]][v[1]]+1:
                    dist[next_v[n][0]][next_v[n][1]] = dist[v[0]][v[1]]+1
                    que.put([next_v[n][0],next_v[n][1]])
for i in range(N):
    print(*dist[i])