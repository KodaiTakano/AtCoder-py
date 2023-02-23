from sys import exit

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = set(A)
# print(A)

ans = 0
for i in range(K):
    if i in A:
        ans+=1
    else:
        break
print(ans)