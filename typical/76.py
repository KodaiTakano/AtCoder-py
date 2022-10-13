from calendar import c
import sys


N = int(input())

A = list(map(int, input().split()))

A*=2
s=[0]
crr=0
for a in A:
    crr+=a
    s.append(crr)
# print(s)
sum=sum(A)//2
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[j]-s[i]>sum//10:
            break
        if s[j]-s[i]==sum//10:
            print("Yes")
            # print(i, j)
            sys.exit()
print("No")
            