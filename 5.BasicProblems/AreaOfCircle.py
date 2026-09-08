from math import pi
import math

def AreaOfCircle(r):
    Area = pi * (math.pow(r,2))
    return Area

print(f"Area of circile 4 :{AreaOfCircle(4)}")
print(f"Area of circile 5 :{AreaOfCircle(5)}")

