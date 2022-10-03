N = int(input())

D:dict={}
for i in range(N):
    S = input()
    if S not in D:
        D[S]=1
        print(i+1)
