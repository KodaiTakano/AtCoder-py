N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))

# 未確認のもの
B=set(A)
C=set(A)

x=A[0]
while(B!=set()):
    while(1):
        x