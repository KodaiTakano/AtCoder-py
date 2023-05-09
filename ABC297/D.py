A, B = map(int, input().split())

ans=0
while(A!=B):
    sub=abs(A-B)
    if A>B:
        if sub%B==0:
            c=sub//B
        else:
            c=sub//B+1
        A-=c*B
    else:
        if sub%A==0:
            c=sub//A
        else:
            c=sub//A+1
        B-=c*A
    ans+=c
    # print(A, B)
print(ans)