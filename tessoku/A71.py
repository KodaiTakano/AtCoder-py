N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
B.reverse()

ans=0
for i in range(N):
    ans+=A[i]*B[i]
print(ans)