import sys

N = int(input())
S=[]
for _ in range(N):
    s = input()
    if s[0] not in ["H", "D", "C", "S"]:
        print("No")
        sys.exit()
    if s[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        print("No")
        sys.exit()
    S.append(s)
S=sorted(S)
for i in range(1, N):
    if S[i-1]==S[i]:
        print("No")
        sys.exit()
print("Yes")

