import sys

S = input()
T = input()
if S==T:
    print("Yes")
    sys.exit()
for i in range(len(S)-len(T)+1):
    if S[i:i+len(T)]==T:
        print("Yes")
        sys.exit()
print("No")