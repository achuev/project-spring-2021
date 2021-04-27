import numpy as np
import matplotlib.pyplot as plt

#constants
C = 8 * (10 ** 8)
I = 1
absR = 1
h = l = 300

def cross(a,b):
    c = vector(0, 0, 0)
    c.x = (a.y * b.z - a.z * b.y)
    c.y = -(a.x * b.z - a.z * b.x)
    c.z = (a.x * b.y - a.y * b.x)
    return c

class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, a):
        return vector(self.x + a.x, self.y + a.y, self.z + a.z)

dfi = vector(0, 0, 0.01)

def dB(R, r, fi):
    return vector((I/C) * (cross(cross(dfi,R),r).x/((r.x * r.x + r.y * r.y + r.z * r.z) ** (3/2))), (I/C) * (cross(cross(dfi,R),r).y/((r.x * r.x + r.y * r.y + r.z * r.z) ** (3/2))), (I/C) * (cross(cross(dfi,R),r).z/((r.x * r.x + r.y * r.y + r.z * r.z) ** (3/2))))

def B(x, y, z):
    fi = 0
    B = vector(0, 0, 0)
    R = vector(absR, 0, 0)
    r = vector(x - R.x, y - R.y, z - R.z)
    while (fi <= 2 * np.pi):
        B = B + dB(R, r, fi)
        fi += dfi.z
        R = vector(absR * np.sin(fi), absR * np.cos(fi), 0)
        r = vector(x - R.x, y - R.y, (-1) * R.z)
    return B

dz = dx = 50
z = dz/2
k = 1
p = 0
x = 0
while (z < h):
    z += dz
    k += 1
while (x > -l):
    x -= dx
    p += 1
p = 2 * p + 1
k = 2 * k
x, z = l - x, h - z
fig, ax = plt.subplots()


for i in range(p):
    for j in range(k):
        ax.arrow(x + i * dx, z + j * dz, 0.5 * 10 ** 18 * -1 * B(x + i * dx, 0, z + j * dz).x, 0.5 * 10 ** 18 * B(x + i * dx, 0, z + j * dz).z, width = 0.5) # -1 - коэффициент подгона, вообще его не должно быть
        #print(B(x + i * dx, 0, z - j * dz).x, B(x + i * dx, 0, z - j * dz).y, B(x + i * dx, 0, z - j * dz).z)
plt.show()