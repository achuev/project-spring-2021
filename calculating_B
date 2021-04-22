import numpy as np
import math
C = 8 * (10 ** 8)
def cross(a,b):
    c = vector(0, 0, 0)
    c.x = (a.y * b.z - a.z * b.y)
    c.y = -(a.x * b.z - a.z * b.x)
    c.z = (a.x * b.y - a.y * b.x)
    return c

def dB(R, r, fi):
    return vector((I/C) * (cross(cross(dfi,R),r).x/((r.x * r.x + r.y * r.y + r.z * r.z) ** (3/2))), (I/C) * (cross(cross(dfi,R),r).y/((r.x * r.x + r.y * r.y + r.z * r.z) ** (3/2))), (I/C) * (cross(cross(dfi,R),r).z/((r.x * r.x + r.y * r.y + r.z * r.z) ** (3/2))))


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, a):
        return vector(self.x + a.x, self.y + a.y, self.z + a.z)


I = 1
dfi = vector(0, 0, 0.0001)
fi = 0
absR = 2
R = vector(absR, 0, 0)
A = vector(float(input()),float(input()),float(input()))
r = vector(A.x - R.x, A.y - R.y, A.z - R.z)
B = vector(0, 0, 0)
dl = cross(dfi, R)
while(fi <= 2*np.pi):
    B = B + dB(R, r, fi)
    fi = fi + dfi.z
    R = vector(absR * np.sin(fi), absR * np.cos(fi), 0)
    r = vector(A.x - R.x, A.y - R.y, A.z - R.z)
print(B.x, "\t", B.y, "\t", B.z)
