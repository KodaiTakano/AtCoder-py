import itertools

def base_n(num_10, n):
    if num_10==0:
        return 0
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

N = int(input())
A = list(map(int, input().split()))

l=[]
for i in range(N-1):
    l.append(i)

ans=100000000000
for i in range(1, N):
    for v in itertools.combinations(l, i):
        OR_list=[]
        OR=0
        k=0
        for j in range(N):
            OR|=A[j]
            if j==v[k]:
                OR_list.append(OR)
                if k!= len(v)-1:
                    k+=1
                OR=0
        OR_list.append(OR)
        XOR=0
        for OR in OR_list:
            XOR^=OR
        # print(v)
        # print(OR_list)
        # print(XOR)
        ans=min(ans, XOR)
print(ans)