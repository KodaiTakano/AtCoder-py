N = int(input())

name=[]
age=[]
for _ in range(N):
    S = list(input().split())
    name.append(S[0])
    age.append(int(S[1]))

tage=age.copy()
tage.sort()
ans=[]
for i in range(N):
    if tage[0]==age[i]:
        print(*name[i:], sep="\n")
        break
    else:
        ans.append(name[i])
print(*ans, sep="\n")