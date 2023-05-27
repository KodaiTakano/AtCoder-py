from collections import defaultdict

N, M, H, K = map(int, input().split())
S = list(input())

usedxy=[0]*M
xy=[set() for _ in range(200001)]
for _ in range(M):
    A = list(map(int, input().split()))
    xy[A[0]].add(A[1])

from sys import exit
import bisect

now=[0, 0]
hp=H
for i in range(N):
    if hp==0:
        print("No")
        exit()
    if S[i]=="R":
        now[0]+=1
    if S[i]=="L":
        now[0]-=1
    if S[i]=="U":
        now[1]+=1
    if S[i]=="D":
        now[1]-=1
    hp-=1
    
    if now[1] in xy[now[0]]:
        if hp<K:
            hp=K
            xy[now[0]].remove(now[1])
            
print("Yes")
        