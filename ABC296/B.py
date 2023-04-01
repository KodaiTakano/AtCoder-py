S=[]
for i in range(8):
    s = list(input())
    S.append(s)

abc="abcdefgh"

for i in range(8):
    for j in range(8):
        if S[i][j]=="*":
            print(abc[j], 8-i, sep="")