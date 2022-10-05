from time import clock_getres


N, M = map(int, input().split())

if N==1 or M==1:
    print(max(N,M))
else:
    print(f'{(N+1)//2*((M+1)//2):.0f}')