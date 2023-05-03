def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

N = int(input())
for _ in range(N):
    x = int(input())
    if is_prime(x):
        print("Yes")
    else:
        print("No")