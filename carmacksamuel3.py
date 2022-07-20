# Prolog
# Author: Samuel Carmack
# Section: 003

# Purpose: 
# Preconditions (inputs): 
# Postconditions (output):

def main():
    print("Press Enter to stop data entry")
    main_list = []
    user_input = input("Enter name, 3 bowling scores with whitespace: ")
    avg_score = 0
    
    if user_input != "":
        
        
        split_input = user_input.split()
        
        split_input_list = [split_input[0], round((float(split_input[1]) + float(split_input[2]) + float(split_input[3]))/3, 2)]
        
        avg_score += split_input_list[1]
        
        if split_input_list[1] >= 150:
            split_input_list.append("yes")
        else:
            split_input_list.append("no")
        
        main_list.append(split_input_list)                    
    
    while user_input != "":
            
        user_input = input("Enter name, 3 bowling scores with whitespace: ")
            
           
        if user_input != "":
            
            split_input2 = user_input.split()
            
            split_input_list2 = [split_input2[0], round((float(split_input2[1]) + float(split_input2[2]) + float(split_input2[3]))/3, 2)]
            
            avg_score += split_input_list2[1]
            
            if split_input_list2[1] >= 150:
                split_input_list2.append("yes")
            else:
                split_input_list2.append("no")
            
        main_list.append(split_input_list2)            
    
    print()
    print("Average Score", round(avg_score, 2))
    print()
    
    print("Bowler  Score   Make the Team?")
    print()
    
    
    for r in range(len(main_list)):
        for c in range(len(main_list[r])):
            print(main_list[r][c], end=" ")
    
    
    
                
main()    