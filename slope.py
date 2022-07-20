# Prolog
# Author: Samuel Carmack
# Section: 003

# Purpose: calculate the slope and distance betwen two points 
# Preconditions (inputs): the coordinates of two points 
# Postconditions (output): prompts for inputs and output distance between two points and the slope of the line betwen them

from math import sqrt

def main():

    # 1. Display introductory message
    print("Slope Calculator")
    print()
    
    # 2. Ask user for first x position
    x1 = float(input("what is first x: "))    

    # 3. Ask user for first y position
    y1 = float(input("what is second y: "))  
    
    # 4. Ask user for second x position
    x2 = float(input("what is second x: "))   
    
    # 5. Ask user for second y position
    y2 = float(input("what is second y: "))    
    
    # 6. Output a blank line 
    print()
    
    # 7. Calculate the distance between the points
    dist_ = sqrt(((y1 - y2) **2) + ((x1 - x2) **2))
    
    # 8. Calculate the slope
    slope_ = ((y1 - y2) / (x1 - x2))
    
    # . Output the distince between the points 
    print ("The distance between the two points is", dist_ ) 
    
    # . Output the slope 
    print ("The slope is", slope_ ) 

main()

# A. The distance between the two points is 7.43303. The slope is -2.8
# B. The distance between the two points is 9. The slope is 0
# C. The distance between the two points is 992.5. The slope is 9925
# D. The distance between the two points is 0. The slope is NaN
