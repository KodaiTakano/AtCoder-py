N = int(input())
S = list(input())

ans=0
for i in range(N-2):
    if S[i]=="R" and S[i+1]=="R" and S[i+2]=="R":
        ans=1
    if S[i]=="B" and S[i+1]=="B" and S[i+2]=="B":
        ans=1

if ans==0:
    print("No")
else:
    print("Yes")