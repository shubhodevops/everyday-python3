
print("\n----------------------------------------------")
print("          Welcome to Theater Show               ")
print("----------------------------------------------")

try:  
    audienceAge= int(input("Enter your age: ")) 
except ValueError:
    print("Invalid Age Format")
    audienceAge=0

if  audienceAge <=0:
    print("Age cannot be zero or negetive one, Try once again")
    exit()
    
audienceClass= "Adult"  if audienceAge >=18 else "Child"

try:
    weekNum = int(input("Enter today's week day(1 for SAT, 2 for SUN ... 7 for FRIDAY): "))
except ValueError:
    weekNum = 0  # Fallback for non-numeric input 

weekDays = "" #taking black variable

if 1<= weekNum <=7:



    if weekNum ==1:
        weekDays="Saturday"
    elif weekNum ==2:
        weekDays="Sunday"
    elif weekNum ==3:
        weekDays="Monday"

    elif weekNum ==4:
        weekDays="Tuesday"

    elif weekNum ==5:
        weekDays="Wednesday"

    elif weekNum ==6:
        weekDays="Thursday"

    elif weekNum ==7:
        weekDays="Friday"    
    else:
        weekDays="Invalid Weekday"
        
else:
    print(f"You are providing Invalid Weekday:{weekNum}")        
    exit()    


ticketPrice =12 if audienceAge >=18 else 8   

discountTicketPrice = ticketPrice-2 if weekNum==5 else ticketPrice

#print(f"Your age is {audienceAge}, and Ticket Price for the day {weekDays} is:{discountTicketPrice} ")


print("\n----------------------------------------------")
print("                TICKET INVOICE                ")
print("----------------------------------------------")
print(f" Category:      {audienceClass} ({audienceAge} years old)")
print(f" Show Day:      {weekDays}")
print(f" Ticket Price:  {discountTicketPrice}$ USD")
print("----------------------------------------------")
    
