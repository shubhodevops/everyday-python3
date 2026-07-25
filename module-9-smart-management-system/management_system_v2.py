


# ==============================================================
# DATA INITIALIZATION (গবেষণামূলক ও তথ্য সংরক্ষণের ডিকশনারি ও সেট তৈরি)
# ==============================================================

# Create an empty dictionary to map student names to their single overall scores
student_tracker = {}  # Format: {"Student Name": score}

# Create an empty dictionary to store names and phone numbers
contact_book = {}  # Format: {"Contact Name": "Phone Number"}

# Create an empty set for inventory categories (Sets automatically remove duplicate values)
product_categories = set()  # Format: {"Category1", "Category2"}

# Create an empty dictionary to tally election votes per candidate
voting_results = {}  # Format: {"Candidate Name": total_votes}

# Create an empty dictionary to store multiple subject marks for students
student_reports = {}  # Format: {"Student Name": [mark1, mark2, ...]}

# Create a tuple holding main menu labels (Tuples are immutable, so choices remain constant)
main_menu = (
    "Add Student Scores",
    "View Score Summary",
    "Manage Contacts",
    "Manage Inventory",
    "Run Voting System",
    "Searching Feature",
    "Student Performance Report",
    "Exit",
)

# Create a tuple for sub-menu options under Contact Book Management
contact_menu = (
    "Add Record",
    "Update Record",
    "Delete Record",
    "View All Records",
    "Return to Main Menu",
)

# Create a tuple for sub-menu options under Inventory Management
inventory_menu = (
    "Add Unique Category",
    "Display Categories",
    "Math Operations (Union & Difference)",
    "Return to Main Menu",
)

# Print visual header divider for the system title
print("\n" + "=" * 62)

# Print application welcome title centered
print("   Welcome to Smart School Management & Voting Analysis System   ")

# Print bottom divider for the system title
print("=" * 62)

# ==============================================================
# MAIN CONTROL LOOP (প্রধান নিয়ন্ত্রণ লুপ)
# ==============================================================

# Start an infinite loop to keep running the application until option 8 (Exit) is chosen
while True:
    # Display the Main Menu header
    print("\n--- MAIN MENU ---")

    # Loop over the tuple options starting index count from 1 instead of 0
    for index, option in enumerate(main_menu, start=1):
        # Print formatted menu option line by line
        print(f"{index}. {option}")

    # Prompt user for their choice and strip surrounding whitespace/newlines
    choice = input("\nEnter your choice (1-8): ").strip()

    # ----------------------------------------------------------
    # 1. ADD STUDENT SCORES
    # ----------------------------------------------------------
    # Check if the user selected Option 1
    if choice == "1":
        # Display header for Option 1
        print("\n--- Add Student Scores ---")

        # Start a loop to validate the number of students to enter
        while True:
            # Begin exception handling for integer conversion
            try:
                # Convert string input to integer
                num_students = int(input("How many students to enter? "))

                # Ensure non-negative count
                if num_students >= 0:
                    # Break validation loop if input is valid
                    break

                # Display error message for negative numbers
                print("Please enter a non-negative number.")

            # Catch value conversion errors if user inputs text instead of numbers
            except ValueError:
                # Display error message for non-integer inputs
                print("Invalid input. Please enter a valid integer.")

        # Loop 'num_students' times to collect individual student entries
        for i in range(num_students):
            # Print current student entry heading (1-indexed)
            print(f"\nEntering details for student {i + 1}:")

            # Validation loop for student name
            while True:
                # Prompt for student name and remove extra trailing/leading spaces
                name = input("Enter student name: ").strip()

                # Ensure name is not empty
                if name:
                    # Exit loop if name is valid
                    break

                # Error message when name is left blank
                print("Name cannot be empty.")

            # Validation loop for student score
            while True:
                # Catch conversion errors for decimal inputs
                try:
                    # Convert input string to float
                    score = float(input(f"Enter score for {name} (0-100): "))

                    # Check range condition (between 0 and 100)
                    if 0 <= score <= 100:
                        # Exit loop if score is within range
                        break

                    # Error message if score is out of 0-100 bounds
                    print("Score must be between 0 and 100.")

                # Catch invalid string input for floats
                except ValueError:
                    # Error message for non-numeric input
                    print("Invalid input. Please enter a valid number.")

            # Save/overwrite student name and score pair into dictionary
            student_tracker[name] = score

        # Print section heading for recorded student data
        print("\nCurrent Student Records:")

        # Iterate over all stored dictionary key-value pairs
        for s_name, s_score in student_tracker.items():
            # Print student name alongside their respective score
            print(f" - {s_name}: {s_score}")

        # Convert dictionary scores to a immutable tuple and display it
        print(f"\nScores Tuple: {tuple(student_tracker.values())}")

    # ----------------------------------------------------------
    # 2. VIEW SCORE SUMMARY
    # ----------------------------------------------------------
    # Check if user selected Option 2
    elif choice == "2":
        # Print header for Option 2
        print("\n--- Score Summary ---")

        # Check if dictionary is empty
        if not student_tracker:
            # Print notice if no student records exist
            print(
                "No student data available. Please add student scores first."
            )

            # Skip remaining block code and jump back to main menu
            continue

        # Extract all dictionary values into a list
        scores = list(student_tracker.values())

        # Find and print the maximum value in the list
        print(f"Highest Score: {max(scores)}")

        # Find and print the minimum value in the list
        print(f"Lowest Score : {min(scores)}")

        # Calculate average (sum of scores divided by count) formatted to 2 decimal places
        print(f"Average Score: {sum(scores) / len(scores):.2f}")

    # ----------------------------------------------------------
    # 3. MANAGE CONTACTS
    # ----------------------------------------------------------
    # Check if user selected Option 3
    elif choice == "3":
        # Start infinite loop for contact book sub-menu navigation
        while True:
            # Display Contact sub-menu title
            print("\n--- Contact Book Menu ---")

            # Display sub-menu options using enumerate
            for i, opt in enumerate(contact_menu, start=1):
                # Print options line by line
                print(f"  {i}. {opt}")

            # Prompt for sub-choice input
            sub_choice = input("Select an option (1-5): ").strip()

            # Contact Sub-option 1: Add new contact
            if sub_choice == "1":
                # Prompt for contact name
                name = input("Enter contact name: ").strip()

                # Check if name is blank
                if not name:
                    # Display error message
                    print("Name cannot be empty.")

                # Check if contact name key already exists in dictionary
                elif name in contact_book:
                    # Display warning message
                    print(
                        "Contact already exists. Use update option to change."
                    )

                # Execute if name is non-empty and unique
                else:
                    # Prompt phone number and assign value to key in contact_book dictionary
                    contact_book[name] = input("Enter phone number: ").strip()

                    # Success confirmation message
                    print(f"Contact '{name}' added successfully.")

            # Contact Sub-option 2: Update existing contact
            elif sub_choice == "2":
                # Prompt for contact name to update
                name = input("Enter contact name to update: ").strip()

                # Verify contact exists in dictionary
                if name in contact_book:
                    # Update dictionary key with new phone input
                    contact_book[name] = input(
                        "Enter new phone number: "
                    ).strip()

                    # Success message
                    print(f"Contact '{name}' updated successfully.")

                # If contact name key does not exist
                else:
                    # Print not found warning
                    print("Contact not found.")

            # Contact Sub-option 3: Delete contact
            elif sub_choice == "3":
                # Prompt for contact name to delete
                name = input("Enter contact name to delete: ").strip()

                # Verify if name key exists in dictionary
                if name in contact_book:
                    # Delete key-value pair from dictionary
                    del contact_book[name]

                    # Deletion success message
                    print(f"Contact '{name}' deleted.")

                # Executed if key is missing
                else:
                    # Print missing contact alert
                    print("Contact not found.")

            # Contact Sub-option 4: Display all saved contacts
            elif sub_choice == "4":
                # Sub-section header
                print("\n--- Contact List ---")

                # Check if contact book dictionary is empty
                if not contact_book:
                    # Display empty notification
                    print("[Contact book is empty]")

                # Execute if dictionary has data
                else:
                    # Loop over key-value pairs in dictionary
                    for k, v in contact_book.items():
                        # Display individual name and phone number record
                        print(f" Name: {k} | Phone: {v}")

            # Contact Sub-option 5: Return to Main Menu
            elif sub_choice == "5":
                # Break out of sub-menu loop
                break

            # Handle invalid selections outside range 1-5
            else:
                # Error alert
                print("Invalid option. Try again.")

    # ----------------------------------------------------------
    # 4. MANAGE INVENTORY
    # ----------------------------------------------------------
    # Check if user selected Option 4
    elif choice == "4":
        # Loop for Inventory Management sub-menu
        while True:
            # Display Inventory sub-menu heading
            print("\n--- Inventory Category Management ---")

            # Loop over inventory menu tuple options
            for x, y in enumerate(inventory_menu, start=1):
                # Print options
                print(f"  {x}. {y}")

            # Prompt user for option choice
            sub_choice = input("Select an option (1-4): ").strip()

            # Inventory Sub-option 1: Add new category
            if sub_choice == "1":
                # Prompt for category string
                cat = input("Enter unique product category: ").strip()

                # Check string is not empty
                if cat:
                    # Add category string to set (Duplicates automatically ignored)
                    product_categories.add(cat)

                    # Confirmation message
                    print(f"Category '{cat}' added.")

            # Inventory Sub-option 2: Display saved categories
            elif sub_choice == "2":
                # Print current set items or fallback text if set is empty
                print(f"Unique Categories: {product_categories or '[Empty]'}")

            # Inventory Sub-option 3: Mathematical Set operations
            elif sub_choice == "3":
                # Header prompt
                print("\nLet's create a Secondary Set to compare with.")

                # Instantiate empty secondary set for comparison
                secondary_set = set()

                # Validation loop for count of secondary items
                while True:
                    # Catch conversion errors
                    try:
                        # Prompt and convert to integer
                        num_items = int(
                            input("How many items for secondary set? ")
                        )

                        # Validate non-negative integer
                        if num_items >= 0:
                            # Break loop if valid
                            break

                        # Prompt error for negative integers
                        print("Please enter a positive number.")

                    # Handle string conversion exceptions
                    except ValueError:
                        # Error alert
                        print("Invalid input. Please enter an integer.")

                # Loop to add specified quantity of items to secondary set
                for i in range(num_items):
                    # Prompt for item string
                    item = input(f"Enter item {i + 1}: ").strip()

                    # Verify string is not empty
                    if item:
                        # Add item into secondary set
                        secondary_set.add(item)

                # Print primary set content
                print(f"\nPrimary Set   : {product_categories}")

                # Print secondary set content
                print(f"Secondary Set : {secondary_set}")

                # Compute and print Union (All distinct combined elements)
                print(
                    f"Union         : {product_categories.union(secondary_set)}"
                )

                # Compute and print Difference (Items in Primary NOT in Secondary)
                print(
                    f"Difference    : {product_categories.difference(secondary_set)}"
                )

            # Inventory Sub-option 4: Exit Sub-menu
            elif sub_choice == "4":
                # Exit loop to main menu
                break

            # Handle unexpected menu choices
            else:
                # Warning prompt
                print("Invalid option. Try again.")

    # ----------------------------------------------------------
    # 5. RUN VOTING SYSTEM
    # ----------------------------------------------------------
    # Check if user selected Option 5
    elif choice == "5":
        # Header display for Voting System
        print("\n--- Run Voting System ---")

        # Loop for validating total voters count
        while True:
            # Exception handler for voter input
            try:
                # Prompt integer input for total voters
                num_voters = int(input("Enter total number of voters: "))

                # Check non-negative value
                if num_voters >= 0:
                    # Exit loop on valid entry
                    break

                # Error alert for negative entries
                print("Please enter a positive number.")

            # Catch value conversion errors
            except ValueError:
                # Display error message
                print("Invalid input. Please enter an integer.")

        # Check edge case for 0 voters
        if num_voters == 0:
            # Print alert
            print("No voting can occur with 0 voters.")

            # Return to main menu
            continue

        # Clear voting dictionary results from any previous session
        voting_results.clear()

        # Loop through each voter to collect votes
        for i in range(num_voters):
            # Inner validation loop to prevent empty vote submission
            while True:
                # Prompt voter for candidate string choice
                candidate = input(
                    f"Voter {i + 1} - Enter candidate name: "
                ).strip()

                # Verify name string is valid
                if candidate:
                    # Exit validation loop
                    break

                # Print error message
                print("Candidate name cannot be empty.")

            # Increment candidate vote count in dictionary safely using dict.get()
            voting_results[candidate] = voting_results.get(candidate, 0) + 1

        # Print election tally header
        print("\n--- Voting Results ---")

        # Iterate over voting results dictionary
        for cand, count in voting_results.items():
            # Print candidate name along with their total votes
            print(f" Candidate '{cand}': {count} vote(s)")

        # Find the max vote count among all recorded candidates
        max_votes = max(voting_results.values())

        # Use list comprehension to gather all candidates matching maximum vote count
        winners = [
            cand
            for cand, count in voting_results.items()
            if count == max_votes
        ]

        # Check if more than one candidate tied for highest votes
        if len(winners) > 1:
            # Print tie results listing tied candidates separated by commas
            print(
                f"\nThe election ended in a Tie between {', '.join(winners)} with {max_votes} votes each!"
            )

        # Executed if only a single candidate achieved highest votes
        else:
            # Print clear winner candidate and max vote total
            print(f"\nWinner: Candidate '{winners[0]}' with {max_votes} votes!")

    # ----------------------------------------------------------
    # 6. SEARCHING FEATURE
    # ----------------------------------------------------------
    # Check if user selected Option 6
    elif choice == "6":
        # Print Search section heading
        print("\n--- Searching Feature ---")

        # Prompt input and normalize string with casefold() for case-insensitive comparison
        query = input("Enter search term: ").strip().casefold()

        # Initialize boolean flag tracker to monitor search success
        found = False

        # Search Module 1: Check student tracker dictionary keys
        for name, score in student_tracker.items():
            # Compare lowercase query string with lowercase name key
            if name.casefold() == query:
                # Print student record if found
                print(f"[Student Tracker] Found '{name}' with score: {score}")

                # Update flag indicator to True
                found = True

        # Search Module 2: Check contact book dictionary keys
        for name, phone in contact_book.items():
            # Case-insensitive comparison check
            if name.casefold() == query:
                # Print contact record if found
                print(f"[Contact Book] Found '{name}' with phone: {phone}")

                # Set flag indicator to True
                found = True

        # Search Module 3: Check voting results dictionary keys
        for cand, votes in voting_results.items():
            # Case-insensitive check
            if cand.casefold() == query:
                # Print election record if found
                print(
                    f"[Voting Ledger] Found candidate '{cand}' with {votes} votes"
                )

                # Set flag indicator to True
                found = True

        # Execute if target query was not matched in any dataset
        if not found:
            # Print non-found notice
            print("Record not found across any module.")

    # ----------------------------------------------------------
    # 7. STUDENT PERFORMANCE REPORT
    # ----------------------------------------------------------
    # Check if user selected Option 7
    elif choice == "7":
        # Section header display
        print("\n--- Student Performance Report ---")

        # Loop for entering multiple student reports
        while True:
            # Prompt for name input or exit trigger string
            student_name = input(
                "\nEnter student name (or 'done' to finish): "
            ).strip()

            # Check if exit command 'done' is entered
            if student_name.casefold() == "done":
                # Exit student entry loop
                break

            # Verify input is not empty string
            if not student_name:
                # Error alert
                print("Student name cannot be empty.")

                # Skip to next iteration
                continue

            # Validation loop for subject quantity
            while True:
                # Catch integer conversion errors
                try:
                    # Prompt number of subjects to input
                    num_subjects = int(
                        input(f"How many subject marks for {student_name}? ")
                    )

                    # Ensure positive non-zero quantity
                    if num_subjects > 0:
                        # Break validation loop
                        break

                    # Error message
                    print("Please enter a number greater than 0.")

                # Catch float/string input errors
                except ValueError:
                    # Display error prompt
                    print("Invalid input. Enter a whole number.")

            # Create temporary list to collect marks for this student
            scores_list = []

            # Loop through specified number of subjects
            for i in range(num_subjects):
                # Inner validation loop for individual mark value
                while True:
                    # Catch float conversion exceptions
                    try:
                        # Prompt mark for subject
                        score = float(input(f"  Subject {i + 1} Mark (0-100): "))

                        # Validate mark within 0 to 100
                        if 0 <= score <= 100:
                            # Append valid score to temporary list
                            scores_list.append(score)

                            # Break inner mark validation loop
                            break

                        # Print range error message
                        print("Score must be between 0 and 100.")

                    # Handle string conversion errors
                    except ValueError:
                        # Print error message
                        print("Invalid input. Enter a number.")

            # Store student name and list of subject marks into dictionary
            student_reports[student_name] = scores_list

        # Check if student performance report dictionary is empty
        if not student_reports:
            # Print notice if empty
            print("\n[No student records entered.]")

        # Execute if student records were entered
        else:
            # Print report top divider
            print("\n" + "=" * 40)

            # Loop over student performance entries in dictionary
            for student, marks in student_reports.items():
                # Formatted list comprehension turning float list into string like "[85.0] [90.0]"
                formatted_marks = " ".join([f"[{m}]" for m in marks])

                # Display student name
                print(f"Student: {student}")

                # Display joined marks list
                print(f" Subject Scores: {formatted_marks}")

                # Display calculated total sum of marks
                print(f" Total Score   : {sum(marks)}")

                # Display calculated average rounded to 2 decimal places
                print(f" Average Score : {sum(marks) / len(marks):.2f}")

                # Print report row divider
                print("-" * 40)

    # ----------------------------------------------------------
    # 8. EXIT
    # ----------------------------------------------------------
    # Check if user selected Option 8
    elif choice == "8":
        # Print exit appreciation text
        print("\nThank you for using the Smart School Management System!")

        # Terminate main application infinite loop
        break

    # Execute if choice is outside the 1 to 8 range
    else:
        # Print invalid selection alert
        print("Invalid input! Please enter a number between 1 and 8.")


