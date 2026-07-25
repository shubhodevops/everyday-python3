
user_input = input("Enter Numbers separated by spaces: ")

num = list(int(n) for n in user_input.split())

counts = {"even": 0, "odd": 0}

for n in num:
    if n % 2 == 0:
        counts["even"] += 1

    else:
        counts["odd"] += 1

print(f"Even: {counts['even']}")
print(f"Odd: {counts['odd']}")