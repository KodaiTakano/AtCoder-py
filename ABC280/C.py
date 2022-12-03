import sys

S = input()
T = input()

for i in range(len(S)):
    if S[i]!=T[i]:
        print(i+1)
        sys.exit()
print(len(T))