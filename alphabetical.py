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
    # store the letters of the word in the value as a list
    words[word] = list(word)

#
##
### sort the words -- we could use sorted method... 
##  but that would have eliminated the point of using a dictionary
#   and would not allow me to practice dictionaries and lists

# taking a bubble sort approach




### TESTING

# Print the resulting dictionary
# print("The dictionary of words and their first letters is:")
# print(words)