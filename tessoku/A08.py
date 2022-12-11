H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

sum=[[0]*(W+1)]
for i in range(H):
    s=[0]
    crr=0
    for j in range(W):
        crr+=X[i][j]
        s.append(crr+sum[i][j+1])
    sum.append(s)
# print(sum)

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(sum[C][D]-sum[A-1][D]-sum[C][B-1]+sum[A-1][B-1])