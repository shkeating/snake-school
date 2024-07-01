# accepts a phrase from user letter-only input with word limit and determines which word in the phrase is the longest by containing the most characters

#while loop ensures the program keeps asking for input until the user provides a valid string.
while True:
    #accepts user input
    user_phrase = input("Please enter a string: ")
    
    try:
        # Check if the input string is not longer than 14 words
        word_count = len(user_phrase.split())
        if word_count >= 14 or word_count <= 0:
            print("The input string is not the right length (at least 1 word, and no longer than than 14 words).") #ensures user sees what they did wrong
            raise ValueError() # makes the program stop and re prompt for input 
    
    except: # prompt user to try again
        print("invalid input. Please try again.")

    else: # Exit the while loop if the input is valid and continue on
        print("Thanks. Let's see which of those words is the longest in character length!")
        break  

#turn user phrase into a list stored in word list variable
words = user_phrase.split() #creates word array from string
longest_word = "" #stores variable for longest word 
max_length = 0 #starging word count for longest word computation

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

# compares word counts and prints out all the users words with how many letters are in them. 
for word, count in zip(words, letter_counts): #zip makes a nested list of the words with their counts paired together
    print(f"The word '{word}' has {count} letters.")
	#f string used to make string interpolation less annoying (or, i guess more like javascript lol)
print(f"The longest word is '{longest_word}' with {max_length} letters.")