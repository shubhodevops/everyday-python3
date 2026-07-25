print("\nSimple Sum Calculator:")
sum_count = 0
while sum_count < 2:
    calculate_num = int(input(f"Enter a number of {sum_count + 1}: "))
    addition = calculate_num + calculate_num
    sum_count += 1
print("\n---------------------------------")
print(f"Largest number is {addition}")
print("---------------------------------")
