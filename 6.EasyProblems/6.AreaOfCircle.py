import math
import numpy as np

def AreaOfCircle(r):
    area = math.pi*(r*82)
    print(f"the area of the circle using math funciton is:",area)
    area = math.pi * math.pow(r, 2)
    print(f"the area of the circle using math  Pow funciton is:",area)
    area = np.pi * (r ** 2)
    print(f"the area of the circle using Numpy funciton is:",area)
    PI = 3.142
    area = PI * (r * r)
    print(f"the area of the circle is:",area)


AreaOfCircle(5)
AreaOfCircle(10)

