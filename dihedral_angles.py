import numpy as np
import math

def cross_product(v1, v2):
    v3 = (v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0])
    return v3

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]


def dihedral_angle(p1, p2, p3, p4):
    """
    Calculate dihedral angle between 4 points (vectors p1-p2-p3-p4).
    Returns angle in degrees.
    """
    b1 = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    b2 = (p3[0] - p2[0], p3[1] - p2[1], p3[2] - p2[2])
    b3 = (p4[0] - p3[0], p4[1] - p3[1], p4[2] - p3[2])  

    print(f"b1: {b1}, b2: {b2}, b3: {b3}")
    
    n1 = cross_product(b1, b2)
    n2 = cross_product(b2, b3)

    print(f"n1: {n1}, n2: {n2}")

    abs_n1 = math.sqrt(n1[0]**2 + n1[1]**2 + n1[2]**2)
    abs_n2 = math.sqrt(n2[0]**2 + n2[1]**2 + n2[2]**2)

    print(f"abs_n1: {abs_n1}, abs_n2: {abs_n2}")

    cos0 = dot_product(n1, n2) / (abs_n1 * abs_n2)
    sin0 = math.sqrt(sum(cross_product(n1, n2)[i]**2 for i in range(3))) / (abs_n1 * abs_n2)

    print(f"cos0: {cos0}, sin0: {sin0}")

    angle = math.degrees(math.atan2(sin0, cos0))

    sign = dot_product(n1, b3) < 0.0

    if sign:
        print("Angle is negative, adjusting sign.")
        angle = -angle 
    
    return angle


a1 = (1, 9, 2)
a2 = (3, 2, 1)  
a3 = (2, 4, 7)  
a4 = (8, 2, 5)
print(f"Dihedral angle: {dihedral_angle(a1, a2, a3, a4)} degrees")

