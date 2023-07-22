N = int(input())
S = list(input())

a=0
b=0
c=0
for i in range(N):
    if S[i]=="A":
        a=1
    if S[i]=="B":
        b=1
    if S[i]=="C":
        c=1
    if a==1 and b==1 and c==1:
        print(i+1)
        break