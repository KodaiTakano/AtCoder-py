H, W, N = map(int, input().split())
A = set()
for _ in range(N):
    a, b = map(int, input().split())
    A.add(10000*(a-1)+b-1)

# print(A)
    
add=[[0]*W for _ in range(H)]
# print(add)

for i in range(H):
    if 10000*i not in A:
        add[i][0]=1
# print(add)

for j in range(W):
    if j not in A:
        add[0][j]=1

# print(add)


for i in range(1, H):
    for j in range(1, W):
        if 10000*i+j not in A:
            l=min(i, j)+1
            add[i][j]=min(l, add[i-1][j]+1, add[i][j-1]+1, add[i-1][j-1]+1)

# print(add)

ans=0
for i in range(H):
    for j in range(W):
        ans+=add[i][j]
print(ans)