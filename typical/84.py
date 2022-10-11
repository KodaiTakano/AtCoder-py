N = int(input())
S = input()

ma = -1
ba = -1
ans = 0
for i in range(len(S)):
    if S[i]=="o":
        if ba!=-1:
            ans += ba
        ma = i+1
    if S[i]=="x":
        if ma!=-1:
            ans += ma
        ba = i+1
print(ans)