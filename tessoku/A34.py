N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


# Grandy:石がi個の時のGrandy数
grandy=[0]*(max(A)+1)

for i in range(max(A)+1):
    # Transit:Grandy数がiとなるような遷移ができるか
    transit=[0,0,0]
    if i>=X:
        transit[grandy[i-X]]=1
    if i>=Y:
        transit[grandy[i-Y]]=1

    if transit[0]==0:
        grandy[i]=0
    elif transit[1]==0:
        grandy[i]=1
    else:
        grandy[i]=2
    
ans=0
for i in range(N):
    ans^=grandy[A[i]]

if ans!=0:
    print("First")
else:
    print("Second")