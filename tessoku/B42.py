N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]

ans=[0]*4
for i in range(N):
    # 表が正、裏が正
    if B[i][0]+B[i][1]>=1:
        ans[0]+=B[i][0]+B[i][1]
    # 表が正、裏が負
    if B[i][0]-B[i][1]>=1:
        ans[1]+=B[i][0]-B[i][1]
    # 表が負、裏が正
    if -B[i][0]+B[i][1]>=1:
        ans[2]+=-B[i][0]+B[i][1]
    # 表が負、裏が負
    if -B[i][0]-B[i][1]>=1:
        ans[3]+=-B[i][0]-B[i][1]

print(max(ans))