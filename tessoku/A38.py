D, N = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

ans=[24]*D

for i in range(N):
    for j in range(B[i][0]-1, B[i][1]):
        if ans[j]>B[i][2]:
            ans[j]=B[i][2]
# print(ans)
print(sum(ans))