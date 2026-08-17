''' Author: Saif A Khan Shubho, Module-12-Assignment, Date: 16 August 2026 '''
import json
import requests

app_name = "Welcome to Smart Text Analyzer & Live Data App"
def print_app_name():
    print("-" * 50)
    print(f" {app_name} ")
    print("-" * 50)

def error_input():
    # Fixed the color code string format (\033[31m makes the text red in terminals)
    print("\033[Invalid input. Please try again.\033[0m")

def run_app():
    print_app_name()

    # Step 3: String Analyzer
    print("\nString Analyzer ::\n")
    user_sentence = input("Enter/paste Your Sentence(s): ").strip()

    if not user_sentence:
        error_input()
    else:
        char_count = len(user_sentence)
        
        words = user_sentence.split()
        word_count = len(words)
        
        clean_sentence = "".join(words).lower()
        is_palindrome = clean_sentence == clean_sentence[::-1]
        
      # Display
        print(f"Total Characters:   {char_count}")
        print(f"Total Words:        {word_count}")
        print(f"Is it a Palindrome? {'Yes!' if is_palindrome else 'No'}\n")

    # Step 4: Sorting Logic
    print("\nSorting Logic ::\n")
    number_input = input("Enter a list of numbers separated by commas (eg: 5, 2, 9): ").strip()
    
    if not number_input:
        error_input()
        return

    try:
        num_list = [float(num.strip()) for num in number_input.split(",")]
    except ValueError:
        error_input()
        return

    ascending_list = sorted(num_list)
    descending_list = sorted(num_list, reverse=True)
    
    print(f"List[Ascending Order]:      {ascending_list}")
    print(f"List[Descending Order]:     {descending_list}\n")


    # Step 5: Algorithmic Thinking
    print("\nAlgorithmic Thinking ::\n")
    
    largest = num_list[0]
    smallest = num_list[0]
    
    for num in num_list:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
            
    print(f"Largest Number Found:   {largest}")
    print(f"Smallest Number Found:  {smallest}\n")


    # Step 6: API Integration
    #Concept inherits from geeksforgeek website
    print("\nAPI Integration ::\n")
    
    # user to typed city name
    city_input = input("Enter a city name to check the weather(eg:Dhaka,Khulna): ").strip().title()
    
    # Fallback for cityName 
    if not city_input:
        print("No city entered. Default , Dhaka.")
        city_input = "Dhaka"
        
    print(f"Fetching live weather data for {city_input.title()}...")
    
    try:
       
        url = f'https://wttr.in/{city_input}?0'
        res = requests.get(url)
 
        print(res.text)
        
    except Exception as err:
        print("Could not fetch live weather data. Please check internet connection.")
        print(f" __Technical info: {err}")
                            
    print("-" * 45)
    print(" Thank you for using the Smart App! Goodbye.")
    print("─" * 45)



if __name__ == "__main__":
    run_app()

