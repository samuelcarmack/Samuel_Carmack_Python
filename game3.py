#purpose - to take the user on an adventure
#Pre-conditions: user inputs choices as integers, 1 or 2 or 4.
#Post-conditions: prompts are displayed, results of actions are displayed, outcome of game is reported

def main():
    print ("Adventure!")
    print()
    print ("You enter a room with 3 doors.")
    print ("Do you take Door #1, Door #2, Door #3?")
    first_choice = input ("> ")
    if first_choice == "1":
        print ("You see a wolf what do you do?")
        print ("1. Run Away")
        print ("2. Attack the wolf")
        second_choice = input ("> ")
        if second_choice == "1":
             print ("You got away! Congrtatulations. you got through the game alive")
        else : 
            print ("You got eaten!")
    elif first_choice == "2":
        print("You see a locked safe. Do you")
        print ("1. Try to carry it away")
        print ("2. Try to open it")
        second_choice = input ("> ")
        if second_choice == "1":
            print ("It's too heavy, you die!")
        else :
            print ("You open the safe. You get 500 pieces of silver")
        
    else :
        print("You see a big troll. Do you")        
        print ("1. Attack the troll")
        print ("2. Say hello")
        second_choice = input ("> ")
        if second_choice == "1":
            print("The troll refuses to fight")
        else :
            print("He gives you a gold ring")
            
    print ("Game Over!")    
    
main()    







# Test Cases 
# A. Door 1, attacks wolf. 
# B. You got eaten! Game over! Sorry you didn't make it! 
# C. Door 2
# D. 1
# E. You try to carry the safe - it's too heavy, you die. Game over! Sorry you didn't make it!
# F. Door 2, open safe
# G. 2
# H. You open the safe - you get 500 pieces of Silver! Game over! Congratulations! you got through the game alive! You got away with 500 pieces of silver!
# I. Door 3, attack the troll
# J. 1
# K. he refuses to fight and walks away, you live. Congratulations! you got through the game alive!
# L. Door 3, Say hello
# M. He gives you the gold ring 
# N. You have a ring! Congratulations! you got through the game alive!


