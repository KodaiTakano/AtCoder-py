from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# d[辺の長さ]=個数
d=defaultdict(int)
for i in range(N):
    d[A[i]]+=1

ans=0
for v in d.values():
    if v>=3:
        # x!/(3!*(x-3)!)
        x=1
        x3=1
        for i in range(1, v+1):
            if i==v-2:
                x3=x
            x*=i
        ans+=x/(6*x3)
print(int(ans))