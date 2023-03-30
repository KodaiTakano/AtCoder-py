S = list(input())

for i in range(0, len(S), 2):
    temp=S[i]
    S[i]=S[i+1]
    S[i+1]=temp
print(*S, sep="")