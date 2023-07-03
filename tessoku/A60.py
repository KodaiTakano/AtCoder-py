from collections import deque

N = int(input())
A = list(map(int, input().split()))

# ([index, price],...)
q=deque()

for i in range(N):
    if i==0:
        print(-1, end=" ")
    else:
        q.append([i-1, A[i-1]])
        while(q!=deque()):
            pop=q.pop()
            # print(pop)
            if pop[1] > A[i]:
                q.append(pop)
                break
        if q==deque():
            print(-1, end=" ")
        else:
            pop=q.pop()
            print(pop[0]+1, end=" ")
            q.append(pop)
              