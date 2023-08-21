from collections import defaultdict

H, W = map(int, input().split())
B = [list(input()) for _ in range(H)]

dh = [defaultdict(int) for _ in range(H)]
# print(dh)
for i in range(H):
    # print(dh)
    for j in range(W):
        dh[i][B[i][j]]+=1
print(dh)

dw = [defaultdict(int) for _ in range(W)]
for j in range(W):
    for i in range(H):
        dw[j][B[i][j]]+=1
print(dw)

for _ in range(H+W):
    for i in range(H):
        if len(dh[i])==1:
            dh[i]=defaultdict(int)
