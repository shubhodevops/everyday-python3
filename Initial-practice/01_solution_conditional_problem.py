print("\n----------------------------------------------")
print("   Citizen Classification in accordance age     ")
print("----------------------------------------------")

citizenName = input("Enter Your Name: ").strip().title()


try:
    citizenAge = int(input("Please provide your age:  "))
except ValueError:
    print("Input type invalid. Please try once again!")
    citizenAge=0 # Fallback for non-numeric input 
    exit()



citizenType="" # Initialize an empty variable to hold the type safely

if citizenAge <= 0:
    print("Age cannot be zero or negative. Please try once again!")
    exit()

elif 1 <= citizenAge <= 12:
    citizenType="Child"

elif 13 <= citizenAge <= 19:
    citizenType="Teenager"

elif 20 <= citizenAge <= 59:
    citizenType="Adult Person"

else:
    citizenType="Senior Citizen"

print("\n----------------------------------------------")
print("                CLASSIFICATION SUMMARY        ")
print("----------------------------------------------")
print(f" Name: {citizenName}")
print(f" Age:  {citizenAge} years old")
print(f" Type: {citizenType}")
print("----------------------------------------------")    


         