from sys import exit

S = list(input())

f=0
for i in range(len(S)):
    if S[i]=="B":
        f=i
        break

e=0
for i in range(len(S)):
    if S[i]=="B":
        e=i

if e%2==f%2:
    print("No")
    exit()

f=0
for i in range(len(S)):
    if S[i]=="R":
        f=i
        break

e=0
for i in range(len(S)):
    if S[i]=="R":
        e=i

for i in range(f, e):
    if S[i]=="K":
        print("Yes")
        exit()
print("No")