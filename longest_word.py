# accepts a phrase from user letter-only input with word limit and determines which word in the phrase is the longest by containing the most characters
user_phrase = ""

#while loop ensures the program keeps asking for input until the user provides a valid string.
while True:
    #accepts user input
    user_phrase = input("Please enter a string: ")
    
    try:
        #check if input is a string
        if not type(user_phrase) is str:
            raise TypeError("Only strings are allowed")
         # Check if the string is not longer than 14 words
        word_count = len(user_phrase.split())
        if word_count >= 14:
            raise ValueError("The input string is too long (15 words or more).")
    
    except: # if it for some reason fails prompt user to try again
        print("invalid input. Please try again.")

    else: # Exit the while loop if the input is valid
        print("Thanks. Let's see which of those words is the longest in character length!")
        break  


