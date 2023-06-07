from collections import deque

q=deque()

Q = int(input())
for _ in range(Q):
    S = list(input().split())
    if S[0]=="1":
        q.append(S[1])
    elif S[0]=="2":
        print(q[0])
    else:
        q.popleft()