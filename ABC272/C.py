N = int(input())
A = list(map(int, input().split()))
l = []
k = []
for i in A:
    if i%2==0:
        l.append(i)
    else:
        k.append(i)  

if len(l)<2 and len(k)<2:
    print(-1)
elif len(l)<2:
    k=sorted(k)
    print(k[-1]+k[-2])
elif len(k)<2:
    l=sorted(l)
    print(l[-1]+l[-2])
else:
    k=sorted(k)
    l=sorted(l)
    print(max(l[-1]+l[-2], k[-1]+k[-2]))
