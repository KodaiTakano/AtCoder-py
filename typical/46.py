N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(N):
    A[i]=A[i]%46
    B[i]=B[i]%46
    C[i]=C[i]%46

a=[0]*46
b=[0]*46
c=[0]*46
for i in range(N):
    a[A[i]]+=1
    b[B[i]]+=1
    c[C[i]]+=1
    
ans=0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46==0:
                ans+=a[i]*b[j]*c[k]
print(ans)