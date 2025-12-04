# inspiration code for Python Unit Testing Project

import math

def surfaceArea(radius):
    """Return the surface area of a sphere given its radius."""
    return 4 * math.pi * (radius ** 2)

def volume(radius):
    """Return the volume of a sphere given its radius."""
    return (4/3) * math.pi * (radius ** 3)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = float(input("Please Enter the radius: "))
    vol = volume(radius)
    area = surfaceArea(radius)
    print(f"Volume of sphere with radius {radius} is {vol:.2f}")
    print(f"Surface area of sphere with radius {radius} is {area:.2f}")

if __name__ == '__main__':
    prompt()
