A = list(map(int, input().split()))

from sys import exit

for i in range(len(A)-1):
    if A[i]>A[i+1]:
        print("No")
        exit()

for a in A:
    if a<100 or 675<a:
        print("No")
        exit()
    if a%25!=0:
        print("No")
        exit()
print("Yes")