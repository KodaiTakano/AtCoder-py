import re
import sys

S = input()

if re.search('[A-Z]', S[0])==None:
    print("No")
    sys.exit()

if len(S)!=8:
    print("No")
    sys.exit()

if re.search('[1-9]', S[1])==None:
    print("No")
    sys.exit()

for i in range(2, len(S)-1):
    if re.search('[0-9]', S[i])==None:
        print("No")
        sys.exit()

if re.search('[A-Z]', S[len(S)-1])==None:
    print("No")
    sys.exit()

print("Yes")