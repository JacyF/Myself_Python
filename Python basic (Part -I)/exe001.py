# 1. Write a Python program to print the following string in a specific format (see the output). 
# Sample String : "Twinkle, twinkle, little star, 
# How I wonder what you are! Up above the world so high, 
# Like a diamond in the sky. 
# Twinkle, twinkle, little star, How I wonder what you are" Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

world = ['Twinkle, twinkle, little star',
         'How I wonder what you are!',
         'Up above the world so high,',
         'Like a diamond in the sky.',
         'Twinkle, twinkle, little star,',
         'How I wonder what you are']

print(f"--> {world[0]}")
print(f"--> {world[1]}")
print(f"--> {world[2]}")
print(f"--> {world[3]}")
print(f"--> {world[4]}")
print(f"--> {world[5]}")
