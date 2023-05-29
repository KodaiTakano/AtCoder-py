M=list(input().split())
C=M[1]
N=int(M[0])
S = list(input())

sum=0
for i in range(N):
    if S[i]=="B":
        sum+=1
    if S[i]=="R":
        sum+=2

if sum%3==0 and C=="W":
    print("Yes")
elif sum%3==1 and C=="B":
    print("Yes")
elif sum%3==2 and C=="R":
    print("Yes")
else:
    print("No")