# accepts a phrase from user letter-only input with word limit and determines which word in the phrase is the longest by containing the most characters

#while loop ensures the program keeps asking for input until the user provides a valid string.
while True:
    #accepts user input
    user_phrase = input("Please enter a string: ")
    
    try:
        # Check if the input string is not longer than 14 words
        word_count = len(user_phrase.split())
        if word_count >= 14:
            print("The input string is too long (15 words or more).") #ensures user sees what they did wrong
            raise ValueError() # makes the program stop and re prompt for input 
    
    except: # if it for some reason fails prompt user to try again
        print("invalid input. Please try again.")

    else: # Exit the while loop if the input is valid
        print("Thanks. Let's see which of those words is the longest in character length!")
        break  

#turn user phrase into a list stored in word list variable
words = user_phrase.split()
longest_word = ""
max_length = 0

#set up list to store letter counts in
letter_counts = []
for word in words:
    # Count the number of letters each of the words
    count = len(word)
    # add the counted letters into the list
    letter_counts.append(count)
    # Check if the current word is longer than the longest word found so far
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

# pairs words with their counts and prints out all the users words with how many letters are in them. f string used to make string interpolation less annoying (or, i guess more like javascript lol)
for word, count in zip(words, letter_counts):
    print(f"The word '{word}' has {count} letters.")

print(f"The longest word is '{longest_word}' with {max_length} letters.")