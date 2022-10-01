N = int(input())
ans = hex(N)[2:].upper()
if(len(ans)==1):
    print('0'+ans, sep="")
else:
    print(ans)