# grade calculator
# # #
# takes in inputs from the user for each item within a category 
# adds up the points earned, divides by the amount possible to get the mean for that category
# and calculates 
# the final course grade using the weights of 
# each type of assignment and the means for each category using their weights

# variable initalization

print("lets figure out your grade in Programming for Problem Solving!")

# assignment type weights
weight_discussion = 0.36
weight_assignment = 0.36
weight_exercise = 0.14
weight_quiz = 0.14


#discussion grades
discussion_points = 36
earned_discussion_points = [0]

#collecting discussion points for the six assignments
while True:
    discuss = input(f"Enter a number of points earned for discussion {len(earned_discussion_points)}): ")
    try:
        discuss = float(discuss)
    except:
        print('Please use numeric digits.')
        continue
    if discuss > 6 or discuss < 0: #make sure it a valid number of points and lwet them reenter if not
        print('Please enter a positive number equal to or less than 6.')
        continue
    if len(earned_discussion_points) >= 6:  #stop collecting values once we have 6
        break
    earned_discussion_points.append(float(discuss))
total_earned_discussion_points = sum(earned_discussion_points)


#assignment grades
assignment_points = 36
    # creates empty list to store the points
earned_assignment_points = [0]

#collecting assignment points for the six assignments
while True:
    assignment = input(f"Enter a number of points earned for assignment {len(earned_assignment_points)}): ")
    try:
        assignment = float(assignment)
    except:
        print('Please use numeric digits.')
        continue
    if assignment > 6 or assignment < 0: #make sure it a valid number of points and lwet them reenter if not
        print('Please enter a positive number equal to or less than 6.')
        continue
    if len(earned_assignment_points) >= 6:  #stop collecting values once we have 6  
        break
    earned_assignment_points.append(float(assignment))
total_earned_assignment_points = sum(earned_assignment_points)

#w3 exercise grade
exercise_points = 14
while True:
    print('Enter points earned on w3 exercises, up to 14 points: ')
    earned_exercise_points = input()
    try:
        earned_exercise_points = float(earned_exercise_points)
    except:
        print('Please use numeric digits.')
        continue
    if earned_exercise_points > 14 or earned_exercise_points < 0:  #make sure it a valid number of points and lwet them reenter if not
        print('Please enter a positive number equal to or less than 14.')
        continue
    break

#w3 quiz grade
quiz_points = 14
while True:
    print('Enter points earned on w3 quiz, up to 14 points: ')
    earned_quiz_points = input()
    try:
        earned_quiz_points = float(earned_quiz_points)
    except:
        print('Please use numeric digits.')
        continue
    if earned_quiz_points > 14 or earned_quiz_points < 0: #make sure it a valid number of points and lwet them reenter if not
        print('Please enter a positive number equal to or less than 14.')
        continue
    break


# earned grades percentage calculations
earned_discussion = total_earned_discussion_points / discussion_points * 100
earned_assignment = total_earned_assignment_points / assignment_points * 100
earned_exercise = earned_exercise_points / exercise_points * 100
earned_quiz = earned_quiz_points / quiz_points * 100

# output points and averages for every category
print(f"the average for discussion posts was {earned_discussion}%, with points totaling to {total_earned_discussion_points} out of 36.")
print(f"the average for weekly assignments was {earned_assignment}%, with points totaling to {total_earned_discussion_points} out of 36.")
print(f"the average for weekly assignments was {earned_quiz}%, with points totaling to {earned_quiz_points} out of 14.")
print(f"the average for weekly assignments was {earned_exercise}%, with points totaling to {earned_exercise_points} out of 14.")

# multiply each percentage by its cooresponding category weight

discussion = weight_discussion * float(earned_discussion)
assignment = weight_assignment * float(earned_assignment)
exercise = weight_exercise * float(earned_exercise)
quiz = weight_quiz * float(earned_quiz)

# sum the categories to get output of numerical grade earned
grade = discussion + assignment + exercise + quiz


#add in the corresponding letter grade to the calculated number
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