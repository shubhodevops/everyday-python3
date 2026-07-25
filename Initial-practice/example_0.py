
# Example of Print() function,Varible Examples+ Datatype example, input() function, escape sequence, type casting example, type() function and id() function
# in addition f-string example()



#Simple expression of print() function

print("welcome to python program") #simple print() function
print('welcome to "Special" python class') #using double quotation
print('''Example of Triple quote usages of ''') #example triple quote
print("hello, it's a dynamic world") #example of single line

#example of variable

firstName ="Saif A" #varible declare with string datatype
lastName="Khan" #varible declare with string datatype
dob='1986-11-14' #varible declare with string datatype
home="Lalmatia" #varible declare with string datatype
workstation="Segunbagicha" #varible declare with string datatype
postCode="1207" #varible declare with string datatype
weeklyIncome=40000.00 #varible declare with floating point datatype
weeklyIncomeTax=weeklyIncome*15/100 #variable assigned as floating point datatype
distanceHomeToWorkstation=7 #varible declare with integer datatype
isTwoDaysWeekend=True # variable declare with boolean datatype

print(f"My Name is {firstName} {lastName} and Date of birth is: {dob}.\nMy workstation is: {workstation} and my home location is: {home}\nand distance between both location: {distanceHomeToWorkstation} km.  ")

#example of input() function
print("What About you?")
fName = str(input("Type Your first name :")).upper()
lName = str(input("Type your Last Name :")).upper()
print(f"Your Full Name is {fName} {lName}")
pCode= str(input("Type Your Post Code :"))
wDays= int(input("Type your Total Weekdays :"))
hourlySalary= float(input("Enter your Per hour Salary :"))

print(f"Your Post code is:{pCode}\nand your weekdays is : {wDays}\nand your weekly Salary is: {hourlySalary*8*wDays} ")

phoneNumber = str(input("First Enter Country Code then Phone Number :")).split()
print(f"Phone Number with Country Code: {phoneNumber}")

#Escape Sequence
print("I'm from Lalmatia\nand I'm going to Segunbagicha")

print("welcome to", end =" ")
print("Bangladesh")

print("CountryCode\tDivisionCode\tDistrictCode")
print("880\t001\t007")

print("apple", "grape","banana", sep=" | ")

#TypeCasting Example
amount = "40000"
convertedAmount = float(amount)#string to float
print(f"amount is: {amount}")
print(type(amount))
print(type(convertedAmount))

monthCode ="01"
convertedMonthCode =int(monthCode)#string to integer
print(f"Month Code is: {monthCode}")
print(type(monthCode))
print(type(convertedMonthCode))

weekDaysCode=5
convertedWeekDaysCode=str(weekDaysCode) #integer to string
print(f"Week Days is: {weekDaysCode}")
print(type(weekDaysCode))
print(type(convertedWeekDaysCode))


isFridayWeekDays = True
convertedIsFridayWeekDays = int(isFridayWeekDays) # boolean to integer
convertedIsFridayWeekDays_2 =float(isFridayWeekDays) # boolean to floating point
convertedIsFridayWeekDays_3=str(isFridayWeekDays) # boolean to string
print(f" is friday weekend?: {isFridayWeekDays}")
print(type(isFridayWeekDays))
print(type(convertedIsFridayWeekDays))
print(type(convertedIsFridayWeekDays_2))
print(type(convertedIsFridayWeekDays_3))

# example of id() function

countryName ="Bangladesh"

print(f"Country name: {countryName} and its Memory reference address is" , id(countryName))














