# Module-8 Assignment
# Author: A Khan Shubho
# Date: 20 July 2026

print("\n------------------------------------")
print("   Welcome to Smart Voting System     ")
print("------------------------------------")

# 📌 Step 3: Voting Data Input
while True:
    try:
        # Prevent non-integer inputs or negative voter numbers
        num_voters = int(input("\nHow many voters will vote? "))
        if num_voters < 0:
            print("Please enter a positive number of voters.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")

votes = list()
# For each voter: Ask for candidate name and store votes in a list.

for i in range(num_voters):
    while True:
        candidate = input(f"Enter candidate name for vote {i+1}: ").strip().lower()

        if not candidate:
            print("Candidate name cannot be empty. Please try again.")
            continue

        votes.append(candidate)
        break

# 📌 Step 4: Frequency Counter Using Dictionary
vote_counts = dict()
for vote in votes:
    if vote in vote_counts:
        vote_counts[vote] += 1
    else:
        vote_counts[vote] = 1


# 📌 Step 5: Display Vote Results
print("\n--- Vote Results ---")
if vote_counts:
    for candidate, count in vote_counts.items():

        print(f"{candidate.title()} : {count}")

else:
    print("No votes were casted.")


# 📌 Step 6: Winner Detection
if vote_counts:
    winner = max(vote_counts, key=vote_counts.get)
    print(f'\n"Winner is Candidate {winner.title()}"')
else:
    print("\nWinner Detection: No winner can be determined because no votes were cast.")


# 📌 Step 7: Searching Feature
search_name = input("\nEnter Candidate name to search their data: ").strip()
if not search_name:
    print("Search query was empty. No data retrieved.")
elif search_name in vote_counts:
    print(
        f"Data Found: Candidate {search_name.title()} received: {vote_counts[search_name]} votes."
    )
else:
    print(f"No voting data found for candidate '{search_name.title()}'.")
