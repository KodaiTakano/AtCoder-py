N = input()
half=len(N)//2
if len(N)==1:
    print(0)
if len(N)%2!=0:
    N=str(10**(len(N)-1)-1)
if len(N)%2==0:
    if int(N[:half])<=int(N[half:]):
        print(int(N[:half]))
    else:
        print(int(N[:half])-1)