S = list(input())
# print(S)
ans=0
i=0
while(i<len(S)):
    # print(i)
    if i < len(S)-1:
        if S[i]=='0' and S[i+1]=='0':
            i+=1
    i+=1
    ans+=1
print(ans)