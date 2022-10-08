import itertools

N, M = map(int, input().split())


attend_list = []
for i in range(M):
    x = list(map(int, input().split()))
    x.pop(0)
    c = itertools.combinations(x, 2)
    for v in itertools.combinations(x, 2):
        attend_list.append(v)

if len(set(attend_list))==N*(N-1)/2:
    print("Yes")
else:
    print("No")