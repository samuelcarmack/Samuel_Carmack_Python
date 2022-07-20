# Prolog
# Author: Samuel Carmack
# Section: 003

# Purpose: calculate how much a customer will spend at a store with and without sales tax
# Preconditions (inputs): y or n for 5 prompts 
# Postconditions (output): prompts for inputs and how much a customer will spend at a store with and without sales tax

def main():
    # 1. display title
    print ("Camping Supply Store")
    print()
    
    # 2. display instructions
    print ("Enter y or n to answer the questions")
    totalWOtax = 0
    
    # 3. ask about walking stick, if yes, add cost to bill 
    first_choice = input ("Do you want a walking stick? ($15) ")
    if first_choice == "y":
        totalWOtax = totalWOtax + 15
    second_choice = input ("Do you want a canteen? ($10) ")
    if second_choice == "y":
        totalWOtax = totalWOtax + 10
    third_choice = input ("Do you want a water filter? ($25) ")
    if third_choice == "y":
        totalWOtax = totalWOtax + 25    
    fourth_choice = input ("Do you want a tent? ($100-$150) ")
    if fourth_choice == "y":
        totalWOtax = totalWOtax + 100
        fifth_choice = input ("Do you want a large tent? ($150) ")
        if fifth_choice == "y":
            totalWOtax = totalWOtax + 50
    # initialize total bill
    
    # calculate sales tax 
    sales_tax = totalWOtax * 0.06  
    totalWtax = totalWOtax + sales_tax
    print()
    
    # display total bill with $ in front
    print("Your total bill is $" + str(totalWOtax))
    
    # display total bill plus tax with $ in front
    print ("Your total bill plus tax is $" + str(totalWtax))
    
    # thank them for their business
    print ("Thank you for your business!")
    
main()