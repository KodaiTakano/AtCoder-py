from collections import deque

q=deque()

N, X = map(int, input().split())
S = list(input())

q.append(X-1)
S[X-1]="@"
while(q!=deque()):
    pos=q[-1]
    q.pop()
    if pos-1>-1:
        if S[pos-1]==".":
            S[pos-1]="@"
            q.append(pos-1)
    if pos+1<N:
        if S[pos+1]==".":
            S[pos+1]="@"
            q.append(pos+1)

print(*S, sep="")