from sys import exit

N, K = map(int, input().split())
A = list(map(int, input().split()))

A = list(set(A))
# print(A)
k=0
for i in range(K):
    if i==len(A):
        break
    if A[i]!=k:
        print(k)
        exit()
    else:
        k+=1
print(k)