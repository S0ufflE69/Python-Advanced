import math

def circle_area(r):
    return int(math.pi * r * r)

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h

r = int(input("Enter circle radius: "))
print("Circle area:", circle_area(r))

a, b = map(float, input("Enter rectangle sides: ").split())
print("Rectangle area:", rectangle_area(a, b))

base, height = map(float, input("Enter triangle base and height: ").split())
print("Triangle area:", triangle_area(base, height))

def analyze_array(arr):
    total = sum(arr)
    mean = total / len(arr)
    return total, mean

for i in range(3):
    arr = list(map(int, input(f"Enter array {i+1}: ").split()))
    s, avg = analyze_array(arr)
    print("Sum:", s, "Mean:", avg)
