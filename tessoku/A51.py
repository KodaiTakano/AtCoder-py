from collections import deque

N = int(input())

q=deque()

for i in range(N):
    Q = list(input().split())
    if Q[0]=="1":
        q.append(Q[1])
    elif Q[0]=="2":
        print(q[-1])
    else:
        q.pop()