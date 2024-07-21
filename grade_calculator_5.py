# grade calculator
# # #
# takes in a text file of assignment grades, or creates one and adds grades to it based on user input prompts
# adds up the points earned, divides by the amount possible to get the mean for that category
# and calculates 
# the final course grade using the weights of 
# each type of assignment and the means for each category using their weights

# provides functions to work with file paths
import os
#imports regex
import re

#provides file path
filename = "grades.txt"

##
###
#### user output start
###
#
print("Let's figure out your grade in Programming for Problem Solving!")
print("...")


#
##
###
#### DATA STRUCTURES
###
##
#


# assignment type weights, stored in dictionary
weight = {
    "discussion": 0.36,
    "assignment": 0.36,
    "exercise": 0.14,
    "quiz": 0.14
}
# assignment quantities, stored in dictionary
quantity = {
    "discussion": 6,
    "assignment": 6,
    "exercise": 1, # only one of these, will leave it be at 1 as an int
    "quiz":  1 # only one of these, will leave it be at 1 as an int
}

# calculates points possible to earn for each assignment type using the values in our quantities dictionary
points = {
    "discussion": quantity["discussion"] * 6,
    "assignment": quantity["assignment"] * 6,
    "exercise": quantity["exercise"] * 14,
    "quiz": quantity["quiz"] * 14
}
    


#initialize dictionary to store earned points
earned_points = {
}

print("...")
print("...") #breaks up output to increase legibility



#
##
###
#### FUNCTIONS
###
##
#

####  reads a text file of grades and converts it into a dictionary format, making it easy to do calculations with them later on in the program

def get_grades_from_file(filename):
    if os.path.exists(filename): 
    # checks if file exists
        with open(filename, 'r') as file: 
        # uses with to replace try/catch in a shorter format that is better for file handling because it will close the file after reading it even if there are issues
            lines = file.readlines() 
            #lines is a list with each line of the file inside of it as a string
            grades = {} 
            # grades is an empty dictionary (for now) that holds our categories and their corresponding points
            for line in lines: 
            # in our lines list, we are going to process the data to make it possible to do computations
                category, *points = line.strip().split() 
                # remove trailing and leading extra spaces from each line, and splits each word in the line into a list based on internal whitespace
                grades[category] = list(map(float, points)) 
                #converts the amounts of points into numbers instead of strings, so they can be used to do math, and assigns the float it is converted to to be associated with its associated category in the grades directory
            return grades 
            # return grades dictionary with categories paired with their points as floats
    return None


#### creates a file with our grades data if we didn't have one to start with. takes a dictionary of grades and writes it to a text file in a structured format
def write_grades_to_file(filename, grades):
    #opens file in write mode, creating it if we don't already have one
    with open(filename, 'w') as file:
        for category, points in grades.items(): 
            # loops through each key and value (categories and points) in our grades dictionary
            points_str = ' '.join(map(str, points)) 
            # converts points values into strings and them joins them into a single string, separated by spaces.
            file.write(f"{category} {points_str}\n") 
            # writes the category and its affliated points as a line in the file, and adds a new line at the end (/n)

#### point collection function for categories with multiple items in them


def collect_points(category, max_points, quantity):
    points = []
    for i in range(quantity):
        while True:
            try:
                point = float(input(f"Enter points earned for {category} {i + 1} (0 to {max_points}): "))
                if 0 <= point <= max_points:
                    points.append(point)
                    break
                else:
                    print(f"Please enter a number between 0 and {max_points}.")
            except ValueError:
                print(f"Invalid input. Please enter a valid number between 0 and {max_points}.")
    return points



#### point collection function for categories with only one item


def collect_points_single(category, max_points):
    while True:
        try:
            point = float(input(f"Enter points earned for {category} (0 to {max_points}): "))
            if 0 <= point <= max_points:
                return point
            else:
                print(f"Please enter a number between 0 and {max_points}.")
        except ValueError:
            print(f"Invalid input. Please enter a valid number between 0 and {max_points}.")

#### calculating percentages function

def calculate_percentages(total_points, points):
    return {key: total_points[key] / points[key] * 100 for key in total_points}

#### calculating weighted points from percentage
def calculate_weighted_scores(percentages, weights):
    return {key: percentages[key] * weights[key] for key in percentages}


#### adds up weighted scores to total score
def calculate_final_grade(weighted_scores):
    return sum(weighted_scores.values())

#### converts final grade score into letter grade
def determine_letter_grade(grade):
    if grade >= 94:
        return 'A'
    elif grade >= 90:
        return 'A-'
    elif grade >= 87:
        return 'B+'
    elif grade >= 83:
        return 'B'
    elif grade >= 80:
        return 'B-'
    elif grade >= 77:
        return 'C+'
    elif grade >= 73:
        return 'C'
    elif grade >= 70:
        return 'C-'
    elif grade >= 67:
        return 'D+'
    elif grade >= 63:
        return 'D'
    elif grade >= 60:
        return 'D-'
    else:
        return 'E'
    

#
##
###
#### PROGRAM EXECUTION
###
##
#



#
###
#### calculations for each assignment type using their functions
###
#

#calls function pulling grade data from file
earned_points = get_grades_from_file(filename)

#falls back to original collection method and writes collected data to file to use from it
if not earned_points:
    earned_points = {
        "discussion": collect_points("discussion", 6, quantity["discussion"]),
        "assignment": collect_points("assignment", 6, quantity["assignment"]),
        "exercise": [collect_points_single("exercise", 14)],
        "quiz": [collect_points_single("quiz", 14)]
    }
    write_grades_to_file(filename, earned_points)
    #writes collected data to file

#
###
#### calling grade calculation functions
###
#

total_points = {key: sum(value) if isinstance(value, list) else value for key, value in earned_points.items()}
percentages = calculate_percentages(total_points, points)
weighted_scores = calculate_weighted_scores(percentages, weight)
final_grade = calculate_final_grade(weighted_scores)
letter_grade = determine_letter_grade(final_grade)

print("Calculating grade...")
print("...")


for key in percentages:
    print(f"The average for {key} was {percentages[key]:.2f}%, with points totaling to {total_points[key]} out of {points[key]}.")
    # the :.2f rounds the flor to the hundredths place
print("...")
print(f'Your final grade calculates to {final_grade:.2f}%. Your letter grade is a(n) {letter_grade}.')