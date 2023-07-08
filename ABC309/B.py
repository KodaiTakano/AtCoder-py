N = int(input())
B = [list(map(int, input())) for _ in range(N)]

a=B[0][N-1]
for i in range(N-1, 0, -1):
    B[0][i]=B[0][i-1]
# print(B)

b=B[N-1][N-1]
for i in range(N-1, 0, -1):
    if i==1:
        B[i][N-1]=a
    else:
        B[i][N-1]=B[i-1][N-1]
# print(B)

c=B[N-1][0]
for i in range(N-1):
    if i==N-2:
        B[N-1][i]=b
    else:
        B[N-1][i]=B[N-1][i+1]
# print(B)

for i in range(N-1):
    if i==N-2:
        B[i][0]=c
    else:
        B[i][0]=B[i+1][0]

[print(*B[i], sep="") for i in range(N)]