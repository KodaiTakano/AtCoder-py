def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def sample(n):
    if n==1:
        return 1
    elif 2<=n<=3:
        return 2
    elif 4<=n<=4:
        return 3
    elif 5<=n<=7:
        return 4
    elif 8<=n<=8:
        return 5
    elif 9<=n<=10:
        return 6
    elif n==11:
        return 7
    elif 12<=n<=15:
        return 8
    elif n==16:
        return 9
    elif 17<=n<=18:
        return 10
    elif n==19:
        return 11
    elif 20<=n<=21:
        return 12
    elif n==22:
        return 13
    elif 23<=n<=24:
        return 14
    elif n==25:
        return 15
    elif 26<=n<=30:
        return 16
    elif n==31:
        return 17
    elif 32<=n<=33:
        return 18
    elif n==34:
        return 19
    elif 35<=n:
        return 20


K = int(input())

fac = factorization(K)
ans=0
for k in fac:
    ans=max(ans, k[0]*sample(k[1]))
print(ans)
