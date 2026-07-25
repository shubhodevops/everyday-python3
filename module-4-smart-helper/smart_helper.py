
# Author: Saif A Khan Shubho
# Date: 17 June 2026

print("\n-----------------------------------------")
print("  Welcome to Smart Daily Helper Toolkit    ")
print("-----------------------------------------")

showMenu="yes" #Variable initialization for controlling the menu loop condition

#while True:
while showMenu=="yes" or showMenu=="y": 

    print("\nToolkit Option:")
    print("1. Calculate Age in Months")
    print("2. Check Voting Eligibility")
    print("3. Find Smallest of Three Numbers")
    #extended section
    print("4. Temperature Converter")

    #menuOption = int(input("\nChoose an option between 1 and 3: "))
    menuOption = int(input("\nChoose an option between 1 and 4: "))

    if menuOption ==1:
        print("\nCalculate Age in Months:")

        userAge= int(input("Enter your age in years: "))

        ageInMonth=userAge*12

        print("\n----------------------------------")
        print(f"Result: Your age in months is {ageInMonth}")
        print("----------------------------------")

    elif menuOption ==2:
        print("\nCheck Voting Eligibility:")

        votingAge =int(input("Enter your age: "))

        eligibilityCheck = "Result: You are eligible to vote." if votingAge >=18 else "Result: You are not eligible to vote."
        
        #Use of Ternary Operator (syntax: value_if_true if condition else value_if_false)
        #first evalutes condition, if it is true: print value from left side of if condition block if it is false: print value from else block

        print("\n-------------------------------------")
        print(eligibilityCheck)
        print("-------------------------------------")

    elif menuOption==3:

        print("\nFind the smallest among three numbers:")
        
        smallest=0 # variable initialize to store updated smallest number 
        counter=0 # variable initialize for defining loop count cycle
        
        while counter<3:
            num = int(input(f"Enter a number of {counter+1}: ")) 
                
            if smallest ==0 or num < smallest:
                smallest = num

                # explanation: Imagine enter the numbers respectively 12, 5, and 8:
                # Loop 1 (num = 12): smallest is 0 is True. skips the right side. smallest becomes 12.
                # Loop 2 (num = 5): smallest is 0 is False. checks 5 < 12, which is True. smallest becomes 5.
                # Loop 3 (num = 8): smallest is 0 is False. checks 8 < 5, which is False. smallest remains 5.

            counter +=1

        print("\n---------------------------------")
        print(f"Result: The smallest number is {smallest}")    
        print("---------------------------------")
    
    
    #extended section 
    elif menuOption==4:
        print("\nTemperature Converter:")
        celsius=int(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print("\n-----------------------")
        print(f"Result: {celsius}°C = {fahrenheit}°F")    
        print("-----------------------")    

    else:
        
        #print("\nInvalid choice! Choose an option between 1 and 3")
        print("\nInvalid choice! Choose an option between 1 and 4")
        continue 
        # Use of "continue" The out-of-range (1-4) input number will be ignored, 
        # and an option menu for user input will be shown.
        # Without using "continue", the system will prompt the user to enter the 
        # showMenu variable.(the next line of code right away)
    
        

    showMenu=input("\nDo you want to solve another problem? (yes/no): ").lower()
    #lower() string method is used convert inputted string in to lower case to avoid case sensitivity

else:    
    print("\nThank you for using Smart Daily Helper Toolkit!")    

