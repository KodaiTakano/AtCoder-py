N, K = map(int, input().split())
A = list(map(int, input().split()))



s=[0]
crr=0
for a in A:
    crr+=a
    s.append(crr)
# print(s)
B=[-1]*N
# print(B)
for i in range(N):
    if i!=0:
        B[i]=B[i-1]

    while B[i]<N-1 and s[B[i]+2]-s[i]<=K:
        B[i]+=1
# print(B)
ans=0
for i in range(N):
    # print(B[i]-i)
    ans+=(B[i]-i+1)
print(ans)