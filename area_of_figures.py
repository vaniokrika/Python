from math import pi

figure = str(input())

if figure == 'square':
    side = float(input())
    area = side * side
    area_final = f"{area:.3f}"
    print(area_final)

elif figure == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
    area_final = f"{area:.3f}"
    print(area_final)

elif figure == 'circle':
    radius = float(input())
    area = pi * radius * radius
    area_final = f"{area:.3f}"
    print(area_final)

elif figure == 'triangle':
    side_a = float(input())
    height_a = float(input())
    area = (side_a * height_a) / 2
    final_area = f"{area:.3f}"
    print(final_area)

