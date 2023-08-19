N = int(input())
A = list(map(int, input().split()))
sum=sum(A)
sum=sum//2
sum+=1
s=0
s_b=0
from sys import exit

for i in range(N):
    s+=A[i]
    if s>=sum:
        print(i+1, sum-s_b)
        exit()
    s_b+=A[i]