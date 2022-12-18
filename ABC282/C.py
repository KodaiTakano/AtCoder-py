N = int(input())
S = list(input())

ok=0
for i in range(N):
    if S[i]=="\"" and ok==0:
        ok=1
        continue
    if S[i]=="\"" and ok==1:
        ok=0
    if S[i]=="," and ok==0:
        S[i]="."
print(*S, sep="")