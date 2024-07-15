# grade calculator
# # #
# takes in inputs from the user for each item within a category 
# adds up the points earned, divides by the amount possible to get the mean for that category
# and calculates 
# the final course grade using the weights of 
# each type of assignment and the means for each category using their weights



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
    "discussion": int(input("How many weekly discussion posts were assigned in the course? ")),
    "assignment": int(input("How many weekly assignments were assigned in the course? ")),
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

earned_points = {
    "discussion": collect_points("discussion", 6, quantity["discussion"]),
    "assignment": collect_points("assignment", 6, quantity["assignment"]),
    "exercise": collect_points_single("exercise", 14),
    "quiz": collect_points_single("quiz", 14)
}


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