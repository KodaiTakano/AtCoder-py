N = int(input())
S = list(input())
Q = int(input())

count=0
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T==1:
        i = (A-1+N*count)%(2*N)
        j = (B-1+N*count)%(2*N)
        # print(S[i])
        # print(S[j])
        temp=S[i]
        S[i]=S[j]
        S[j]=temp
    if T==2:
        count+=1
if count%2==0:
    print(*S, sep="")
else:
    print(*S[N:], *S[:N], sep="")