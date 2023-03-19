N, Q = map(int, input().split())

# 0:呼ばれていない人 1:呼ばれた人 2:行った人
state=[0]*N

# 呼ばれたひと
called=set()
# 呼ばれてない人
uncalled=set(range(1,N+1))
first=1

for i in range(Q):
    # print("i=",i)
    # print(called)
    # print(uncalled)
    
    A = list(map(int, input().split()))
    if A[0]==1:
        called.add(first)
        uncalled.remove(first)
        if uncalled!=set():
            first = next(iter(uncalled))
    elif A[0]==2:
        x = A[1]
        called.remove(x)
    else:
        print(next(iter(called)))