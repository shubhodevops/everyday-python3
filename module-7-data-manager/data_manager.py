# Module-6 Assignment
# Author: Saif A Khan Shubho [01316345325]
# Date: 12 JuLY 2026

print("\n--------------------------------------------------")
print("    Welcome to Smart Contact & Inventory Manager    ")
print("--------------------------------------------------")

# 📌 Step 3:
contacts = dict() # initialization dictionary
global name # defined the name as a global variable so that the entire code block name variable can be utilized

# number of contacts
num_contacts = int(input("How many contacts do you want to add? "))

# for Loop to collect contact details, just because, limit defined by input, otherwise while loop
for i in range(num_contacts):
    name  = input(f"Enter name for contact {i+1}: ").lower().strip()
    phone_number = input(f"Enter phone number for {name.title()}: ").strip()
    contacts[name] = phone_number

# 📌 Step 4: Display All Contacts
print("\n--- Contact List ---")
print(f"{'\nName':<20} Phone Number")
print("-" * 32)
for name, phone_number in contacts.items():
    print(f"{name.title():<19} {phone_number}")
print("-" * 32)

# 📌 Step 5: Update and Delete Contact
print("\n--- Update & Delete Operations ---")


# Update operation
name = input("\nWhich contact to update? ").lower().strip()
#Reuses the global name variable to accept a target name for update
if name in contacts:
    new_phone = input(f"Enter new phone number for {name.title()}: ").strip()
    contacts[name] = new_phone
    print(f"Contact {name.title()} updated successfully.")
else:
    print(f"Contact '{name.title()}' not found.")

# Delete operation
name = input("\nWhich contact to delete? ").lower().strip()
#Reuses the global name variable to accept a target name for deletion
if name in contacts:
    del contacts[name]
    print(f"Contact '{name.title()}' deleted successfully.")
else:
    print(f"Contact '{name.title()}' not found.")

# Display final state of contacts after modifications
print("\n--- Updated Contact List ---")
print(f"{'\nName':<20} Phone Number")
print("-" * 32)
for name, phone_number in contacts.items():
    print(f"{name.title():<19} {phone_number}")
print("-" * 32)


# 📌 Step 6: Inventory Categories (Set)
print("\n--- Inventory Categories ---")

# categories based on set
categories = {"electronics", "food", "clothes"}
print(f"Current categories: {categories}")

# add a new category into a set collection
new_category = input("Enter a new product category to add: ")
categories.add(new_category.strip().lower())
print(f"Updated categories: {categories}")

# 📌 Step 8: Nested Dictionary
print("\n--- Product Details (Inventory) ---")
inventory = {
    "Laptop": {"price": 50000, "stock": 10},
    "Phone": {"price": 30000, "stock": 20}
}

# Print product details
for product, details in inventory.items():
    print(f"Item: {product}")
    print(f"  Price: {details['price']} BDT")
    print(f"  Stock: {details['stock']} units")
    print("-" * 22)
