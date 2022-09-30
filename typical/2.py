import numpy as np

H, W = map(int, input().split())
A=[]
for i in range(H):
    A.append(list(map(int, input().split())))

rowsum = [sum(row) for row in A]
colsum = [sum(col) for col in zip(*A)]

ans=np.array(A)
ans*=-1
for i in range(H):
    ans[i]+=rowsum[i]
for i in range(W):
    ans.T[i]+=colsum[i]
    
for ary in ans:
    print(*ary)