# 4. Write a Python program that calculates the area of a circle 
# based on the radius entered by the user.
# Sample Output : 
# r = 1.1
# Area = 3.8013271108436504

from math import pi

r = float(input("Please introduce the value of radius to calculate the area of a circle :"))
print(f"Area = {round((pi*r**2),2)}")
