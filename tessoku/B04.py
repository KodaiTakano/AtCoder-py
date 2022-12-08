def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

N = int(input())
print(base_10(N, 2))