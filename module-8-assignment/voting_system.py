from collections import Counter

# 1. Base Structures: Initialized empty for 100% dynamic live registration
voting_booth = {}
registered_voters = set()  # Dynamically populated by the administrator
voted_citizens = set()     # Tracks live voting activity to prevent fraud

print("=============================================")
print("     ELECTION INITIALIZATION & CONFIG       ")
print("=============================================")

# --- DYNAMIC REGISTRATION PHASE ---
while True:
    print("\n--- REGISTRATION MENU ---")
    print("1. Add a New Voting Position (e.g., President)")
    print("2. Add a Candidate to an Existing Position")
    print("3. Register an Eligible Voter ID")
    print("4. View Current Ballot & Voter Roll Configuration")
    print("5. Lock Configuration & Start Live Voting")
    
    reg_choice = input("Select an option (1-5): ").strip()
    
    if reg_choice == "1":
        new_pos = input("Enter the name of the new position: ").strip().title()
        if not new_pos:
            print("❌ Position name cannot be blank.")
        elif new_pos in voting_booth:
            print(f"❌ '{new_pos}' already exists.")
        else:
            # Building the nested dictionary structure dynamically
            voting_booth[new_pos] = {"Candidates": [], "Votes": {}}
            print(f"✅ Position '{new_pos}' successfully created.")
            
    elif reg_choice == "2":
        if not voting_booth:
            print("❌ Create at least one position first.")
            continue
            
        print("\nAvailable Positions:")
        for idx, position in enumerate(voting_booth.keys(), 1):
            print(f"  {idx}. {position}")
            
        pos_input = input("Enter the exact position name to add a candidate to: ").strip().title()
        
        if pos_input in voting_booth:
            new_cand = input(f"Enter candidate name running for {pos_input}: ").strip().title()
            if not new_cand:
                print("❌ Candidate name cannot be blank.")
            elif new_cand in voting_booth[pos_input]["Candidates"]:
                print(f"❌ '{new_cand}' is already registered for this position.")
            else:
                # Append to candidates list and initialize an empty vote tracking list
                voting_booth[pos_input]["Candidates"].append(new_cand)
                voting_booth[pos_input]["Votes"][new_cand] = []
                print(f"✅ Candidate '{new_cand}' registered for {pos_input}.")
        else:
            print("❌ Invalid position name.")
            
    elif reg_choice == "3":
        # Dynamic Voter Registration Logic
        new_voter = input("Enter a new Voter ID to register (e.g., Voter101): ").strip()
        if not new_voter:
            print("❌ Voter ID cannot be blank.")
        elif new_voter in registered_voters:
            print(f"❌ '{new_voter}' is already a registered voter.")
        else:
            registered_voters.add(new_voter)
            print(f"✅ Voter '{new_voter}' successfully added to the official voter roll.")
            
    elif reg_choice == "4":
        print("\n--- CURRENT BALLOT CONFIGURATION ---")
        if not voting_booth:
            print("  Empty Ballot: No positions or candidates registered yet.")
        else:
            for pos_idx, (position, data) in enumerate(voting_booth.items(), 1):
                print(f"  [{pos_idx}] Position: {position}")
                if not data["Candidates"]:
                    print("       (No candidates registered yet)")
                for cand_idx, candidate in enumerate(data["Candidates"], 1):
                    print(f"       {cand_idx}. {candidate}")
                    
        print("\n--- OFFICIAL VOTER ROLL ---")
        if not registered_voters:
            print("  No voters registered yet.")
        else:
            print(f"  Total Registered: {len(registered_voters)}")
            print(f"  Voter IDs: {', '.join(sorted(list(registered_voters)))}")
                    
    elif reg_choice == "5":
        # Configuration Validation Rules
        incomplete = False
        if not voting_booth:
            print("❌ Cannot lock. You must add at least one position.")
            incomplete = True
        if not registered_voters:
            print("❌ Cannot lock. You must register at least one eligible voter.")
            incomplete = True
            
        for pos, data in voting_booth.items():
            if not data["Candidates"]:
                print(f"❌ Position '{pos}' has no candidates registered!")
                incomplete = True
                
        if incomplete:
            continue
            
        print("\n🔒 Configuration locked successfully! Polling booth is now open...")
        break
    else:
        print("❌ Invalid configuration option. Please select 1-5.")


print("\n=============================================")
print("         POLLING STATION NOW OPEN             ")
print("=============================================")

# --- INTERACTIVE LIVE VOTING PHASE ---
while True:
    print("\n--- LIVE VOTING KIOSK ---")
    print("1. Cast a Vote")
    print("2. Close Election & View Final Tally")
    
    choice = input("Select an option (1-2): ").strip()
    
    if choice == "1":
        print("\n--- VOTER VERIFICATION SYSTEM ---")
        voter_id = input("Enter your Voter ID: ").strip()
        
        # Validates against the dynamically registered list
        if voter_id not in registered_voters:
            print("❌ Access Denied: This ID is not in the registered voter roll.")
            continue
            
        if voter_id in voted_citizens:
            print("❌ Access Denied: Fraud alert! You have already cast your ballot.")
            continue
            
        print("✅ Identity Verified. Please cast your ballot.")
        
        # Nested loop with enumerate() to dynamically cycle through user-created categories
        for pos_index, (position, data) in enumerate(voting_booth.items(), 1):
            print(f"\n[{pos_index}] Position: {position}")
            print("   Available Candidates:")
            
            for cand_index, candidate in enumerate(data["Candidates"], 1):
                print(f"     {cand_index}. {candidate}")
                
            while True:
                try:
                    cand_choice = int(input(f"Select candidate number for {position}: "))
                    if 1 <= cand_choice <= len(data["Candidates"]):
                        selected_candidate = data["Candidates"][cand_choice - 1]
                        
                        # Store vote directly into dynamically built nested dict
                        voting_booth[position]["Votes"][selected_candidate].append(voter_id)
                        print(f"👍 Vote for {selected_candidate} recorded.")
                        break
                    else:
                        print("❌ Invalid candidate number. Try again.")
                except ValueError:
                    print("❌ Please enter a valid number.")
        
        voted_citizens.add(voter_id)
        print(f"\n🎉 Ballot successfully cast for {voter_id}! Thank you.")

    elif choice == "2":
        confirm = input("\nAre you sure you want to close the election? (y/n): ").strip().lower()
        if confirm == 'y':
            break
    else:
        print("❌ Invalid main menu option. Please enter 1 or 2.")


print("\n=============================================")
print("         ELECTION CLOSED: FINAL RESULTS       ")
print("=============================================")

# --- COUNTER & FREQUENCY TALLY PHASE ---
for position, data in voting_booth.items():
    print(f"\n📊 Results Tally for {position}:")
    
    vote_frequency = Counter()
    
    for candidate, voter_list in data["Votes"].items():
        vote_frequency[candidate] = len(voter_list)
    
    for candidate, count in vote_frequency.items():
        print(f" -> {candidate}: {count} vote(s)")
        
    if vote_frequency:
        winner, winner_votes = vote_frequency.most_common(1)[0]
        if winner_votes == 0:
            print(" 🚫 NO WINNER: No votes were cast for this position.")
        else:
            print(f" 🏆 WINNER: {winner} with {winner_votes} vote(s)!")

print("\nThank you for using the fully dynamic Python Voting System!")



# Dynamic Voter Roll Architectureregistered_voters = set(): Instead of hardcoding "Voter1", "Voter2", etc., 
# it starts completely empty. Option 3 adds users live to this verification set.Pre-Flight Lockout (Option 5): 
# The system checks if registered_voters is empty before finalizing setup. 
# You cannot open an election if there are zero registered citizens eligible to vote.Live Cross-Referencing: 
# When option 1 is launched in the voting booth, the user input is validated directly against your custom-built dynamic voter set database.
