from math import atan, sin, degrees, radians
import numpy as np


T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
s=np.array([X,Y,0])
for i in range(Q):
    E = int(input())
    t=np.array([0,-L/2*sin(radians(360*E/T)),abs(L/2*sin(radians(180*E/T)))])
    u=np.array([0,-L/2*sin(radians(360*E/T)),0])
    print(t, u)
    tan=atan(np.linalg.norm(t-u)/np.linalg.norm(s-u))
    print(degrees(tan))