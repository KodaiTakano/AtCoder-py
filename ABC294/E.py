L, N1, N2 = map(int, input().split())

v1=[]
l1=[]
for i in range(N1):
    N, M = map(int, input().split())
    v1.append(N)
    l1.append(M)

v2=[]
l2=[]
for i in range(N2):
    N, M = map(int, input().split())
    v2.append(N)
    l2.append(M)

# li=l1[0]
# lj=l2[0]
# i=0
# j=0
# ans=0
# while(True):
#     if li==lj:
#         if v1[i]==v2[j]:
#             ans+=min(l1[i], l2[j])
#         i+=1
#         j+=1
#         if i>=N1 or j>=N2:
#             break
#         li+=l1[i]
#         lj+=l2[j]
#     elif li<lj:
#         if v1[i]==v2[j]:
#             ans+=l1[i]
#         i+=1
#         if i>=N1 or j>=N2:
#             break
#         li+=l1[i]
#     else:
#         if v1[i]==v2[j]:
#             ans+=l2[j]
#         j+=1
#         if i>=N1 or j>=N2:
#             break
#         lj+=l2[j]
#     # print(i, j)
#     # print(li, lj)
#     # print(v1[i], v2[j])
#     # print(l1[i])
#     # print(ans)
# print(ans)

ans=0
i, j=0, 0
p, q=0, 0
while i<N1 and j<N2:
    if v1[i]==v2[j]:
        ans+=min(p+l1[i], q+l2[j])-max(p, q)
    if p+l1[i]<q+l2[j]:
        p+=l1[i]
        i+=1
    else:
        q+=l2[j]
        j+=1
print(ans)