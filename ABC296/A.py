N = int(input())
S = list(input())

from sys import exit

f = S[0]
for i in range(1, N):
    if f==S[i]:
        print("No")
        exit()
    f=S[i]
print("Yes")