from sys import exit

N, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

ans=0
for a in range(1, 101):
    for b in range(1, 101):
        c=0
        for i in range(N):
            if a-K<=B[i][0]<=a and b-K<=B[i][1]<=b:
                c+=1
        ans=max(ans, c)
        # if ans==4:
        #     print(a, b)
        #     exit()

print(ans)