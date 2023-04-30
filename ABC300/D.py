def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

N = int(input())

C=int(pow(N, 0.5))+1

p=sieve_of_eratosthenes(C)
m=len(p)
ans=0
for a in range(m-2):
    for b in range(a+1, m-1):
        for c in range(b+1, m):
            if pow(p[a],2)*p[b]*pow(p[c],2)>N:
                break
            else:
                ans+=1
        if pow(p[a],2)*p[b]>N:
            break
    if pow(p[a],2)>N:
        break
    
print(ans)