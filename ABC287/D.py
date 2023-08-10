S = list(input())
T = list(input())
SN=len(S)
TN=len(T)

bad=set()
for i in range(TN):
    if S[SN-TN+i]=="?" or T[i]=="?" or S[SN-TN+i]==T[i]:
        continue
    else:
        bad.add(i)

ans=[]
if bad==set():
    ans.append("Yes")
else:
    ans.append("No")

for i in range(TN):
    if i in bad:
        bad.remove(i)
    
    if S[i]!="?" and T[i]!="?" and S[i]!=T[i]:
        bad.add(i)
    
    if bad==set():
        ans.append("Yes")
    else:
        ans.append("No")

print(*ans, sep="\n")