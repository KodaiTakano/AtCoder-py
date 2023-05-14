def base_n(num_10, n):
    if num_10==0:
        return 0
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return str_n[::-1]

def base_10(num_n, n):
    num_10 = 0
    for s in num_n:
        if s==-1:
            s=0
        num_10 *= n
        num_10 += int(s)
    return num_10

S = list(input())
N = int(input())

ans=[-1]*len(S)
for i in range(len(S)):
    if S[i]=="0":
        ans[i]=0
    if S[i]=="1":
        ans[i]=1

# print(base_10(ans, 2))

from copy import deepcopy

for i in range(len(ans)):
    if ans[i]==-1:
        tans=deepcopy(ans)
        tans[i]=1
        # print(tans)
        # print(base_10(tans, 2))
        if base_10(tans, 2)<=N:
            ans[i]=1
# print(ans)
if base_10(ans, 2)<=N:
    print(base_10(ans, 2))
else:
    print(-1)