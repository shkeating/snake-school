#
##
###
#### word alphabetizer
###  takes user input of words and then sorts them into 
##   alphabetical order based on the first letter in each word
#

#
##
### user output start
##
#

print("...")
print("Let's get some words sorted into alphabetical order!")
print("...")
print("...")
print("You can enter as many words as you like, and type a '0' to finish and have your words sorted")
print("...")

#
##
### data structure initialization
##
#

words = dict()

"""
the dictionary data formal will look like this when populated:

words = {
    "cat": ['c', 'a', 't'],
    "egg": ['e','g','g'],
    "rat": ['r','a','t']
}

"""


#
##
### collect words and populate dictionary
##
# TO DO ADD VALIDATION

while True:
    # prompt the user for word input, and remove any extra whitespace with the strip method
    word = input("Enter any word, or enter 0 to finish: ").strip()
    if word == "0":
        break
    # store the letters of the word in the value as a list, see comment in data structures for example of intended data structure
    words[word] = list(word)

joined_letters = ' '
for key in words: #iterate through the keys in the dictionary
    for value in key: #iterate into list
        for letters in value: #iterate through list
            joined_letters += ' ' + letters




print("...")
print("Thanks for all those words! Time to get sorting.")
print("...")
print(joined_letters) # showing the user all the letters back for dramatic effect.. i didn't end up needing those lists of letters.. might as well use them for something. dictionaries are unordered so I actually cant refer to them by index like how i thought i could going into this. I thought I'd be able to use the letters in the lists to do more manual letter comparison and went to bubble sort instead
print("...")
print("Done!")


#
##
### sort the words -- we could use sorted method... 
##  
#  

#   taking a bubble sort approach. we absolutely could use sorted method
#   but that would have not let me practice dictionaries and lists as much
#   which would have eliminated the point of the assignment

# Extract the keys (words) from the dictionary, bubble sort is easier to do with a list
words_list = list(words.keys())

l = len(words_list) #gets the length of our list

for i in range(l): #outer loop that iterates through each word in our list of words
    for j in range(0, l-i-1): #inner loop where we compare and sort
         if words_list[j] > words_list[j+1]: #checking the word against the next word in the list
             #if it starts with a letter further up in the order they get switched
              words_list[j], words_list[j+1] = words_list[j+1], words_list[j]

# Since we can't change the order of our original dictionary we will make a new one that uses the new order of our words list and the data from our original list
sorted_words = {word: words[word] for word in words_list}

#
##
### give the user back their sorted list
##  
#  

sorted_keys = sorted_words.keys()  # grab keys to use in string
sorted_keys_string = ' '.join(sorted_keys) #joins the keys into a string that i can use as output without decorators

print("Here is your sorted list of words, in alphabetical order:")
print(sorted_keys_string)
print("...")
print(f"Your word highest in alphabetical order is {words_list[0]}")