N = int(input())
N_l=[]
for s in str(N):
    N_l.append(int(s))
# print(N)
ans=0
# 最大の桁
ans+=N_l[0]*((N-N_l[0]*pow(10,len(N_l)-1))+1)
for i in range(N_l[0]-1, 0, -1):
    ans+=i*pow(10, len(N_l)-1)

# それ以降の桁
for i in range(1, len(N_l)):
    A=0
    for j in range(i):
        A+=N_l[j]*pow(10, i-j-1)
    for j in range(10):
        # ans+=j*(何回現れたか)
        if N_l[i]<j:
            ans+=j*A*pow(10, len(N_l)-i-1)
        if N_l[i]==j:
            # d:あまり
            d=N
            for k in range(i+1):
                d-=N_l[k]*pow(10, len(N_l)-k-1)
            d+=1
            ans+=j*(A*pow(10, len(N_l)-i-1)+d)
        if N_l[i]>j:
            ans+=j*(A+1)*pow(10, len(N_l)-i-1)
            
print(ans)