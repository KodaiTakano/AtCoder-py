S = list(input())

for s in S:
    if s not in ["a", "e", "i", "o", "u"]:
        print(s, end="")