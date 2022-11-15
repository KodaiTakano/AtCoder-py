S = input()
N=len(S)
count=0
for i in range(N):
    if S[N-i-1]=="0":
        count+=1
    else:
        break
S=S[:N-count]

if S[::-1]==S:
    print("Yes")
else:
    print("No")