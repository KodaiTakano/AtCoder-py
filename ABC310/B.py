N, M = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(N)]

ans=0
for i in range(N):
    for j in range(N):
        ok=1
        if i!=j:
            if B[i][0]>=B[j][0]:
                for bi in B[i][2:]:
                    if bi not in B[j][2:]:
                        ok=0
                if ok:
                    if B[i][0]>B[j][0] or B[i][1]<B[j][1]:
                        ans=1

if ans:
    print("Yes")
else:
    print("No")