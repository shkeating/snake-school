# accepts a phrase from user letter-only input with word limit and determines which word in the phrase is the longest by containing the most characters

## collect input from user to get our words

def get_valid_input(prompt, min_words=1, max_words=14):
    while True:
        user_input = input(prompt)
        words = user_input.split()
        if min_words <= len(words) <= max_words:
            print("Thanks. Let's see which of those words is the longest in character length!")
            return words
        else:
            print(f"The input string is not the right length (at least {min_words} word, and no longer than {max_words} words). Please try again.")
    