# accepts a phrase from user letter-only input with word limit and determines which word in the phrase is the longest using the sorted function

#
## functions
#

## collect input from user to get our words

def get_valid_input(prompt, min_words=1, max_words=14):
    while True:
        #prompt user for words list
        user_input = input(prompt)
        #splits the input string into a list called words
        words = user_input.split()
        if min_words <= len(words) <= max_words:
            print("Thanks. Let's see which of those words is the longest in character length!")
            #show user their input words
            return words
        else:
            print(f"The input string is not the right length (at least {min_words} word, and no longer than {max_words} words). Please try again.")

## sorts our collected words (using the sorted function this time!!) much shorter!

def find_longest_word(words):
    #sorting our words list, key=len sorts the strings by length, setting reverse to true puts them in descending order, ensuring the longest word is first in the list
    sorted_words = sorted(words, key=len, reverse=True) 
    #returns our longest word, and returns an empty string if our user input was empty so we don't get an error for an empty list
    return sorted_words[0] if sorted_words else "" 

#
## program execution
#

#create words list off the get valid input function
words = get_valid_input("Please enter a string: ")

#loop through our list of words and show the number of letters in each word using the len function on each word in the list
for word in words:
    print(f"The word '{word}' has {len(word)} letters.")

#uses the find longest word function to find the longest word in our list
longest_word = find_longest_word(words)

# find the number of letters in our longest word to show the user
max_length = len(longest_word)

#prints what the longest word in the string is and returns it to the user to give them their result
print(f"The longest word is '{longest_word}' with {max_length} letters.")