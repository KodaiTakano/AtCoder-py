import sys
S = input()
S = S[::-1]
for i in range(len(S)):
    if S[i]=="a":
        print(len(S)-i)
        sys.exit()
print(-1)