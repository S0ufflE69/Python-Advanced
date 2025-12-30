import math

def triangle_area(a):
    return (math.sqrt(3) / 4) * a * a

a = float(input("Enter side of hexagon: "))
hexagon_area = 6 * triangle_area(a)
print("Hexagon area:", hexagon_area)

for i in range(1, 4):
    a = float(input(f"Rectangle {i} side a: "))
    b = float(input(f"Rectangle {i} side b: "))
    print(f"Area of rectangle {i}:", a * b)
