import sys
import math

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N = int(input())
A = list(map(int, input().split()))

g = math.gcd(A[0], A[1])
for i in range(1, len(A)):
    g = math.gcd(g, A[i])
for i in range(len(A)):
    A[i]//=g
    
ans = 0
for a in A:
    for i in factorization(a):
        if i[0] not in [1, 2, 3]:
            print(-1)
            sys.exit()
        if i[0] in [2, 3]:
            ans+=i[1]
        
print(ans)
