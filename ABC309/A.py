N, M = map(int, input().split())
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
if N%3!=0 and M-N==1:
    print("Yes")
else:
    print("No")