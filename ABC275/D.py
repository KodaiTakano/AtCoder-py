from functools import lru_cache

@lru_cache
def f(i):
    if i==0:
        return 1
    return f(i//2)+f(i//3) 

N = int(input())
print(f(N))