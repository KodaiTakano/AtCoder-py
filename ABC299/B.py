N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
ans=-1
num=-1
for i in range(N):
    if C[i]==T:
        if num<R[i]:
            ans=i+1
        num=max(num, R[i])
        

if num==-1:
    for i in range(N):
        if C[i]==C[0]:
            if num<R[i]:
                ans=i+1
            num=max(num, R[i])

print(ans)