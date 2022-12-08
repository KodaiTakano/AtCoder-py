def base_n(num_10, n):
    if num_10==0:
        return 0
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return str_n[::-1]

N = int(input())
ans=base_n(N, 2)
for i in range(10-len(ans)):
    print("0", sep="", end="")
print(ans)

