from collections import defaultdict

S = list(input())
N=len(S)
for i in range(N):
    S[i]=int(S[i])

count = [[0]*10 for _ in range(N+1)]

for i in range(N):
    for j in range(10):
        count[i+1][j]=count[i][j]
    if count[i][S[i]]==0:
        count[i+1][S[i]]=1
    else:
        count[i+1][S[i]]=0
    # print(i)
    # [print(*count[j]) for j in range(N+1)]

d = defaultdict(int)
for i in range(N+1):
    d["".join(map(str, count[i]))]+=1
    # print("".join(map(str, count[i])))
# print(d)

ans = 0
for v in d.values():
    ans+=v*(v-1)/2
print(int(ans))