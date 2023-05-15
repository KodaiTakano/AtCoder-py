import itertools

N, M = map(int, input().split())

setl=[set()]*M
for i in range(M):
    C = int(input())
    A = list(map(int, input().split()))
    setl[i]=set(A)
# print(setl)

ans=0
for pro in itertools.product((0, 1), repeat=M):
    c=set()
    for i in range(M):
        if pro[i]==1:
            c|=setl[i]
    if len(c)==N:
        ans+=1
print(ans)