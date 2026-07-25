#Business:
#fruits status(ripe, unripe or overripe) based on color

import string
fruit=input("Enter Fruit Name: ").lower().strip()

color=input("Enter Color Name: ").lower().strip()
fruitStatus=""


if color=="yellow":
    fruitStatus="ripe"
elif color=="green":
    fruitStatus="unripe"
else:
    fruitStatus="overripe"

print(f"Fruit:{fruit.capitalize()} is {fruitStatus.title()}")


###################################################################
#Here’s an example dictionary with multiple fruits and their color-based ripeness rules:
'''
Flexible mapping: Each fruit has its own ripeness rules.
Unknown handling: If the fruit or color isn’t in the dictionary, 
it returns “Unknown status.”
This makes your program much more realistic and adaptable across different fruits.
'''
fruit = input("Enter Fruit Name: ").lower().strip()
color = input("Enter Color Name: ").lower().strip()

#dictionary
ripeness_rules = {
    "banana": {"green": "Unripe", "yellow": "Ripe", "brown": "Overripe"},
    "apple": {"green": "Unripe", "red": "Ripe", "brown": "Overripe"},
    "mango": {"green": "Unripe", "yellow": "Ripe", "black": "Overripe"},
    "grape": {"green": "Unripe", "purple": "Ripe", "brown": "Overripe"},
    "orange": {"green": "Unripe", "orange": "Ripe", "brown": "Overripe"},
    "pineapple": {"green": "Unripe", "yellow": "Ripe", "brown": "Overripe"},
    "pear": {"green": "Unripe", "yellow": "Ripe", "brown": "Overripe"},
    "papaya": {"green": "Unripe", "orange": "Ripe", "black": "Overripe"},
    "tomato": {"green": "Unripe", "red": "Ripe", "brown": "Overripe"},
    "watermelon": {"green": "Unripe", "dark green": "Ripe", "yellow": "Overripe"}
}

fruitStatus = ripeness_rules.get(fruit, {}).get(color, "Unknown status")
print(f"Fruit: {fruit.capitalize()} is {fruitStatus}")
