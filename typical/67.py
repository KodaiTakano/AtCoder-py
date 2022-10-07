def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

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

N, K = map(int, input().split())
for i in range(K):
    N = str(base_n(base_10(N, 8), 9)).replace('8', '5')
print(int(N))

