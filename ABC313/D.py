N, K = map(int, input().split())

res=[]
for i in range(N):
    q=[]
    for j in range(K):
        if i+j>=N:
            j-=N
        q.append(i+j+1)
    # print(q)
    
    print("?", *q)
    # A = list(map(int, input().split()))
    # res.append(A)

res=[0,0,0,0,1]

