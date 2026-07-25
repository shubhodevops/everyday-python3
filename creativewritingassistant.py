#list=[]
    # Description: An ordered, changeable (mutable) collection that allows duplicate items.
    # Ideal for maintaining a specific sequence of data.
    # Declaration:python# Empty list
    # my_list = []
    # # List with items
    # words_list = ["apple", "banana", "apple"]

#Dictionary{}
    # Description: An ordered* collection of key-value pairs that does not allow duplicate keys. Ideal for mapping relationships (like words to their counts).
    # Note: Dictionaries are ordered as of Python 3.7+ (they remember insertion order).
    # Declaration:python
    #
    # # Empty dictionary
    # my_dict = {}
    #
    # # Dictionary with items
    # word_counts = {"apple": 3, "banana": 1}


#tuple=()
    # A tuple is another built-in Python data type.
    # In the context of your script, tuples are highly relevant because Counter.most_common() outputs them, and you can easily convert your unique words into one.
    # Key Characteristics of a Tuple Immutable: Once you create a tuple, you cannot change, add, or remove its items.
    # Ordered: It maintains the exact sequence in which the items were placed.
    # Allows Duplicates: Like a list, it can hold the same word multiple times.
    # You can declare a tuple in Python by placing your items inside parentheses () separated by commas

    # The most common way to create a tuple
    # words_tuple = ("apple", "banana", "cherry")
    # empty_tuple = ()
    #
    #
    # Tuple Without Parentheses (Tuple Packing)Python automatically treats comma-separated values as a tuple,
    # even without brackets
    # packed_tuple = "apple", "banana", "cherry"

#set={}
    #
    # Description: An unordered, unchangeable*, and unindexed collection that does not allow duplicates. Ideal for removing duplicates and testing membership.
    # Note: While set items are unchangeable, you can add or remove items.\
    # Declaration:python
    # # Empty set (MUST use set(), using {} creates a dict)
    # my_set = set()
    #
    # # Set with items
    # words_set = {"apple", "banana", "cherry"}

"""
Phase_1:
Using Features of Variables, input() function, lower() method, split() method, strip() method, replace() method, len() method, set() datatype,
most_common() method and Counter() collections. (submit before:12 June)
# print(f"Sentences in total :{sentenceCount}")
# print(f"The quantity of words in your provided sentences : {numberOfWords} Words")
# print(f"A sentence's typical word count :{numberOfWords/sentenceCount}" )
# print(f"Number of distinct words in the sentences you provided : {len(uniqueWords)} Words")
# print(f'List of distinct words in the sentences you provided : {uniqueWords}')  #Sets use curly braces {} without key-value colons, and they do not maintain a reliable order.
# print(f'List of words that appear more than once in the sentences you provided : {moreThanOnce}') # standard Python dictionary output
# print(f'Top most popular words : {topMost}') # return output as a list of tuples
# print(f"Characters in number : {characters}")
# print(f"Letter count (without spaces): {letters}")
# print(f"Typical Word Length : {avgWordLen}")
# print(f"The article's longest word : {longestWord}")
# print(f"The article's shortest word : {shortestWord}")

phase_2:
# Find the longest and shortest sentence
# Count how many sentences are questions (?) or exclamations (!)
# List all words that start with a capital letter
# Remove duplicate sentences
# Warn the user if a sentence is too long (e.g. more than 20 words)
# Warn if the same word appears more than 3 times
# Check if the text starts and ends with a proper sentence ender (. ! ?)
# Count vowels and consonants in the text
# Count punctuation marks (., !, ?)
# Check if the text has any numbers in it
# Let the user search for a specific word and see how many times it appears


phase_3:
# Adverb overuse detector (-ly words)

phase_4:
phase_5:
phase_6:
phase_7:
"""

from collections import Counter
#collections.Counter is the best and most standard method in Python for counting words.
#High Performance: It is written in C under the hood, making it significantly faster than manual loops.

print("\n-----------------------------------------")
print('Welcome to a "Creative writing assistant" ')
print("-----------------------------------------")

paragraph = input("Enter/paste Your Sentence(s):\n")

#fundamental operation
lowerCaseWords=paragraph.lower().strip() # convert into lowercase and remove whitespace
#strip() method removes all leading (at the start) and trailing (at the end) whitespace from a string.
punctuationFreeWords=lowerCaseWords.replace(".","").replace(",","").replace("?","").replace("!","").replace("(","").replace(")","").replace("()","")# punctuation replace
words=punctuationFreeWords.split() # split into words

#1_countTotalWords
numberOfWords=len(words)

#2_uniqueWords
uniqueWords=set(words)

#3_repeatedWords where more than 1 and top most_common words
repeatedWords=Counter(words)
moreThanOnce = {word: count for word, count in repeatedWords.items() if count > 1}
topMost=repeatedWords.most_common(3) # number of top most_common using parameter value (3 or 5 or user's requirement)

#4_Total sentences and average words used in sentence (Total Words ÷ Total Sentences).
sentenceCount=paragraph.count('.')+paragraph.count('?')+paragraph.count('!')

#5_Characters
characters=" "

#06_Letters (no spaces)
letters=" "

#07_Average Word Length
avgWordLen=" "

#08_Longest Word name
longestWord=" "

#09_Shortest Word Name
shortestWord =" "


#Phase One Completion Date: 7th June 2026
print("\n-----------------------------------------")
print('             Phase One Summary             ')
print("-----------------------------------------")
print(f"Sentences in total :{sentenceCount}")
print(f"The quantity of words in your provided sentences : {numberOfWords} Words")
print(f"A sentence's typical word count :{numberOfWords/sentenceCount}" )
print(f"Number of distinct words in the sentences you provided : {len(uniqueWords)} Words")
print(f'List of distinct words in the sentences you provided : {uniqueWords}')  #Sets use curly braces {} without key-value colons, and they do not maintain a reliable order.
print(f'List of words that appear more than once in the sentences you provided : {moreThanOnce}') # standard Python dictionary output
print(f'Top most popular words : {topMost}') # return output as a list of tuples

print(f"Characters in number : {characters}")
print(f"Letter count (without spaces): {letters}")
print(f"Typical Word Length : {avgWordLen}")
print(f"The article's longest word : {longestWord}")
print(f"The article's shortest word : {shortestWord}")

"""
print("\n-----------------------------------------")
print('             Phase Two Summary             ')
print("-----------------------------------------")

"""