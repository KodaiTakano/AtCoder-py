import itertools

def is_square(v0, v1, v2, v3):
    if v0[0]*v1[0]+v0[1]*v1[1]==0 and v0[0]**2+v0[1]**2==v1[0]**2+v1[1]**2 and v2[0]*v3[0]+v2[1]*v3[1]==0 and v2[0]**2+v2[1]**2==v3[0]**2+v3[1]**2:
        return True
    else:
        return False 

S=[]
for i in range(9):
    s = input()
    for j in range(9):
        if s[j]=='#':
            S.append([i, j])

count=0
for v in itertools.combinations(S, 4):
    v0 = [v[1][0]-v[0][0], v[1][1]-v[0][1]]
    v1 = [v[2][0]-v[0][0], v[2][1]-v[0][1]]
    v2 = [v[1][0]-v[3][0], v[1][1]-v[3][1]]
    v3 = [v[2][0]-v[3][0], v[2][1]-v[3][1]]
    if is_square(v0, v1, v2, v3):
        # print(v[0], v[1], v[2], v[3])
        count+=1
print(count)