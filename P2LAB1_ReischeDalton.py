 # Dalton Reische
 # 6/19/2024
 # P2LAB1
 # Calculating diameter, circumference and area of a circle given the radius
 # User enters the radius
user_radius = float(input('What is the radius of the circle? '))
 # Calculates the diameter, circumference and area based of the users input
import math
cir_diameter = 2 * user_radius
cir_circumference = 2 * math.pi * user_radius
cir_area = math.pi * user_radius ** 2
# Displays the results to the user
print()
print('The diameter of the circle is', end = ' ')
print(f'{cir_diameter:.1f}')
print()
print('The circumference of the circle is', end = ' ')
print(f'{cir_circumference:.2f}')
print()
print('The area of the circle is', end = ' ')
print(f'{cir_area:.3f}')


