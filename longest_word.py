# accepts a phrase from user letter-only input with word limit and determines which word in the phrase is the longest by containing the most characters

phrase = input ("Enter a sentence, phrase, series of words not exceeding 14 words in length")

try:
    word_list = phrase.split()
except:
    print('Please enter a phrase using alphbetical characters')
else: 
    if word_list.length > 14 
        print("Please try again with a shorter phrase, the limit is 14 words.")