# accepts a phrase from user letter-only input with word limit and determines which word in the phrase is the longest by containing the most characters
phrase = ""

#while loop ensures the program keeps asking for input until the user provides a valid string.
while True:
    #accepts user input
    user_phrase = input("Please enter a string: ")
    
    try:
        #check if input is a string
        if not type(user_phrase) is str:
            raise TypeError("Only strings are allowed")