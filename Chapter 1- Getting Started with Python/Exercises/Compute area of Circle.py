from math import pi

# Prompt the user to input the radius of the circle
radius = float(input("Input the radius of the circle: "))

# Calculate the area of the circle
area = pi * radius ** 2

# Display the result, including the radius and calculated area using formatted strings
print(f"The area of the circle with radius {radius} is: {area}")