# Prolog
# Names: Samuel Carmack
# Section: 3

from math import e

# 3 P's for function 1
# Purpose: To define a function that prints value of t and p(t)
# Preconditions: None
# Postconditions: Outputs the t-value next to the solution to the equation

def pop1(t):
    solution = 1/(1 + (e ** (-t)))
    print(solution)

# 3 P's for function 2
# Purpose: To define a function that returns the value of p(t) 
# Preconditions: None
# Postconditions: The value of p(t) from -6 to 6, all added up with the statement "total is" 

def pop2(t):
    solution = 1/(1 + (e ** (-t)))
    return solution

# 3 P's for function 3
# Purpose: To define a function that changes the value of p(t) into a list to be modified later
# Preconditions: None
# Postconditions: The values of p(t) from -6 to 6, all added up with the statement " The second total is" 

def pop3(t, result):
    result[0] = 1/(1 + (e ** (-t)))

def main():
    for t in range(-6, 7):
        print(t, " ", end="")
        pop1(t)
        
    total = 0
    for t in range(-6, 7):
        result = pop2(t)
        total += result
    
    print("Total is", total)     
          
    result = [0]
    total = 0
    for t in range(-6, 7):
        pop3(t, result)
        total += result[0]
    print("The second total is", total)    
    
main()
    