MOD = 1000000007
N = int(input())

a=1
b=1
for _ in range(N-2):
    c=a+b
    c%=MOD
    a=b
    b=c
print(c)