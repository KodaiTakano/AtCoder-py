H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

ans=[0]*min(H,W)
center=set()

for i in range(1, H-1):
    for j in range(1, W-1):
        if A[i][j]=="#" and A[i+1][j+1]=="#" and A[i+1][j-1]=="#" and A[i-1][j+1]=="#" and A[i-1][j-1]=="#":
            n=2
            while(-1<i-n and i+n<H and -1<j-n and j+n<W):
                if A[i+n][j+n]=="#" and A[i+n][j-n]=="#" and A[i-n][j+n]=="#" and A[i-n][j-n]=="#":
                    n+=1
                else:
                    break
            ans[n-2]+=1
print(*ans)