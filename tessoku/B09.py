N = int(input())
B = [[0]*(1501) for _ in range(1501)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    B[a][b]+=1
    B[a][d]-=1
    B[c][d]+=1
    B[c][b]-=1

# [print(B[i][:6]) for i in range(6)]

for i in range(1, 1501):
    for j in range(1501):
        B[i][j]+=B[i-1][j]

for i in range(1501):
    for j in range(1, 1501):
        B[i][j]+=B[i][j-1]

# [print(B[i][:15]) for i in range(15)]

ans=0
for i in range(1500):
    for j in range(1500):
        if B[i][j]>=1:
            ans+=1
print(ans)