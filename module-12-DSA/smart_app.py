"""Author: Saif A Khan Shubho | Module-12-Assignment | Date: 18 August 2026"""


import requests

APP_NAME = "Smart Text Analyzer & Live Data App" # global constant for app name
CLOSING_MSG = "Thank you for using the Smart App! Goodbye." # global constant for closing message
DEFAULT_CITY = "Dhaka" # as a default city for weather data
WEATHER_TIMEOUT = 10 # seconds timeout for weather API requests


def print_app_name(): # function to print the app name with formatting
    print("-" * 50)
    print(f" Welcome to {APP_NAME}\n ")


def error_input(message="Invalid input. Please try again."): #parameterized error message function
    print(f"\033[31m ERROR: {message}\033[0m")
    
    
def print_section(title): # every section's title printing function
    print(f"\n{title} ::")
    print("-" * 22)


def analyze_string(sentence): # fuction to analyze the string for character count, word count and palindrome check
    char_count = len(sentence)
    words = sentence.split()
    word_count = len(words)
        
    clean_sentence = "".join(words).lower() # remove spaces and convert it into lowercase format.
    is_palindrome = clean_sentence == clean_sentence[::-1] # check if the cleaned sentence is equal to its reverse.

    print(f"Total Characters:   {char_count}")
    print(f"Total Words:        {word_count}")
    print(f"Is it a Palindrome? {'Yes!' if is_palindrome else 'No'}\n")


def parse_number_list(raw_input): # function to parse a comma-separated string of numbers into a list of floats or integers
    if not raw_input: 
        return None # return None for empty input

    try:
        num = []
        for part in raw_input.split(","):
            part = part.strip()
            if not part:
                continue
            value = float(part)
            num.append(int(value) if value.is_integer() else value) # convert to int if the float is a whole number
        return num if num else None # return None for empty list after parsing

    except ValueError as e:
        print(f"Error: {e}") 
        return None



def sort_numbers(num): # function to sort a list of numbers in ascending and descending order
    asc = sorted(num) 
    des = sorted(num, reverse=True)

    print(f"List[Ascending Order] :     {asc}")
    print(f"List[Descending Order]:     {des}\n")


def find_largest_smallest(num): # function to find the largest and smallest numbers in a list of num values.
    largest = num[0] # initialize largest and smallest with the first element of the list
    smallest = num[0]

    for n in num:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n

    print(f"Largest Number Found :  {largest}")
    print(f"Smallest Number Found:  {smallest}\n")


def fetch_weather(city): # function to fetch live weather data from wttr.in API for a given city
    url = f"https://wttr.in/{city}?format=3" 
    response = requests.get(url, timeout=WEATHER_TIMEOUT)
    response.raise_for_status() # raise an exception for HTTP errors (4xx or 5xx)
    return response.text.strip() # return the weather data as a string, stripping any leading/trailing whitespace


def run_string_analyzer(): # function to run the string analyzer section of the app
    print_section("String Analyzer")
    sentence = input("Enter/paste Your Sentence(s): ").strip()

    if not sentence: # check for empty input
        error_input("Sentence cannot be empty.")
        return False

    analyze_string(sentence)
    return True


def run_sorting_logic(): # function to run the sorting logic section of the app
    print_section("Sorting Logic")
    
    # Using a loop so the app doesn't crash or quit on bad input!
    while True:
        raw = input("Enter a list of numbers separated by commas (eg: 5, 2, 9): ").strip()
        num = parse_number_list(raw)

        if num is not None:
            sort_numbers(num)
            return num
        
        error_input("Please enter valid comma-separated numbers.")


def run_algorithmic_thinking(num): # function to run the algorithmic thinking section of the app
    print_section("Algorithmic Thinking")
    find_largest_smallest(num)


def run_api_integration(): # function to run the API integration(weather) section of the app
    print_section("API Integration")

    city = input("Enter a city name to check the weather (eg: Dhaka, Khulna): ").strip().title()

    if not city: # check for empty input and use default city
        print(f"No city entered. Using default: {DEFAULT_CITY}.")
        city = DEFAULT_CITY

    print(f"Fetching live weather data for {city}...")

    try:
        weather = fetch_weather(city)
        print(weather)
    except requests.Timeout:
        print("Request timed out. Please try again later.")
    except requests.RequestException:
        print("Could not fetch live weather data. Please check internet connection.")





def run_app(): # main function to run the entire app
    print_app_name()

    run_string_analyzer()

    num = run_sorting_logic() # run sorting logic and get the list of numbers

    run_algorithmic_thinking(num)

    run_api_integration()
    
    

    print("-" * 45)
    print(f" {CLOSING_MSG}")
    print("-" * 45)


if __name__ == "__main__": # entry point of the script
    run_app()
