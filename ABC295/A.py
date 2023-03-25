N = int(input())
A = list(input().split())

from sys import exit

for a in A:
    if a in ["and", "not", "that", "the", "you"]:
        print("Yes")
        exit()
print("No")    