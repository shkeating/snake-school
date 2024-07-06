# grade calculator
# # #
# takes in inputs from the user for each item within a category 
# adds up the points earned, divides by the amount possible to get the mean for that category
# and calculates 
# the final course grade using the weights of 
# each type of assignment and the means for each category using their weights

##
###
#### data structure initalization
###
#

print("Let's figure out your grade in Programming for Problem Solving!")


# assignment type weights, stored in dictionary
weight = {
    "discussion": 0.36,
    "assignment": 0.36,
    "exercise": 0.14,
    "quiz": 0.14
}
# assignment quantities, stored in dictionary
quantity = {
    "discussion": int(input("how many weekly discussion posts were assigned in the course? ")),
    "assignment": int(input("how many weekly assignments were assigned in the course? ")),
    "exercise": 1, # only one of these, will leave it be at 1 as an int
    "quiz":  1 # only one of these, will leave it be at 1 as an int
}

# calculates points possible to earn for each asssignment type using the values in our quantities dictionary
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


##
###
#### discussion posts
###
#

print("We will start by entering your points earned on your discussion posts. They are worth 6 points each")
  #creates varibale to rep dictionary value for points earned list for easuer use in computations

  
  #initalizes earned points key value pair for dicussions
earned_points["discussion"]=[]

#collecting discussion points for the amount set by the user in the quantity dictionary
for i in range(quantity["discussion"]):
    discuss = input(f"Enter a number of points earned for discussion {i + 1}): ")
    try:
        discuss = float(discuss)
    except:
        print('Please use numeric digits.')
        continue
    if discuss > 6 or discuss < 0: #make sure it a valid number of points and lwet them reenter if not
        print('Please enter a positive number equal to or less than 6.')
        continue #To do: fix this it does not stop the input from being accepted
    earned_points['discussion'].append(float(discuss))
    i+=1
    

print("...")
print("...")

#assignment grades
print("Next, we will enter in your points for each weekly assignment. They are worth 6 points each.")

  #initalizes earned points key value pair for dicussions
earned_points["assignment"]=[]

#collecting assignment points for the amount set by the user in the quantity dictionary
for i in range(quantity["assignment"]):
    assign = input(f"Enter a number of points earned for assignment {i + 1}): ")
    try:
        assign = float(assign)
    except:
        print('Please use numeric digits.')
        continue
    if assign > 6 or assign < 0: #make sure it a valid number of points and let them reenter if not
        print('Please enter a positive number equal to or less than 6.')
        continue
    earned_points['assignment'].append(float(assign))
    i+=1

print("...")
print("...")


#w3 exercise grade, take input from user, validate it, and add it to earned points dictionary
print("Just two more left to enter! The w3 exercise completion is worth 14 points. How many did you earn?")
while True:
    print('Enter points earned on w3 exercises, up to 14 points: ')
    exer = input()
    earned_points["exercise"] = exer
    try:
        earned_points["exercise"] = float(earned_points["exercise"])
    except:
        print('Please use numeric digits.')
        continue
    if earned_points["exercise"] > 14 or earned_points["exercise"] < 0:  #make sure it a valid number of points and lwet them reenter if not
        print('Please enter a positive number equal to or less than 14.')
        continue
    break


print("...")
print("...")

#w3 quiz grade. take input from user, validate it, and add it to earned points dictionary
while True:
    print('Last one! Enter points earned on the w3 quiz, up to 14 points: ')
    quiz = input()
    earned_points["quiz"] = quiz
    try:
         earned_points["quiz"] = float(earned_points["quiz"])
    except:
        print('Please use numeric digits.')
        continue
    if  earned_points["quiz"] > 14 or  earned_points["quiz"] < 0: #make sure it a valid number of points and lwet them reenter if not
        print('Please enter a positive number equal to or less than 14.')
        continue
    break

print("Calculating grade...")
print("...")
print("...")
print("...")
print("Done!")

#dictionary storing total point totals computations

total_points = {
    "discussion": sum(earned_points['discussion']),
    "assignment": sum(earned_points['assignment']),
    "exercise": earned_points['exercise'],
    "quiz": earned_points['quiz']
}
print(f"total discussion points is {total_points['discussion']}")

# earned grades percentage calculations
percent = {}

for key in total_points:
    percent[key] = total_points[key] / points[key] * 100
    #calculates percent by dividing points attainable by total points earned for the category, and then multiply by 100 to get their percentage value out of 100
print(percent)

#loop through dictionary, display percentage for each category, points earned, and points possible for each category
for key in percent:
    print(f"the average for {key} was {percent[key]}%, with points totaling to {total_points[key]} out of {points[key]}.")


# loop through percentages and multiply them by their weights. 

weighted = {}

for key in percent:
   weighted[key] = percent[key] * weight[key]

# sum the categories to get output of numerical grade earned
  # initialize variable for grade
grade = 0
 # loop through weighted values dictionary to total up the points and assign to the grade variable
for num in weighted.values():
    grade += num #loops through each vlaue and adds the next until we have grabbed all the vlaues out of the weighted scores dictionary


#add in the corresponding letter grade to the calculated number
  #initalize letter grade variable as a string
letter_grade=""

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'



#print final grade info
print(f'Your final grade calculates to {str(grade)} %. Your letter grade is a {letter_grade}')