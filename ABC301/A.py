N = int(input())
S = list(input())

t=0
a=0
for i in range(N):
    if S[i]=="T":
        t+=1
    else:
        a+=1

if t<a:
    print("A")
elif t>a:
    print("T")
elif S[N-1]=="T":
    print("A")
else:
    print("T")