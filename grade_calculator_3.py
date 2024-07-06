# grade calculator
# # #
# takes in inputs from the user for each item within a category 
# adds up the points earned, divides by the amount possible to get the mean for that category
# and calculates 
# the final course grade using the weights of 
# each type of assignment and the means for each category using their weights

# variable initalization

print("Let's figure out your grade in Programming for Problem Solving!")

# assignment type weights, stored in dictionary
deliverable_weight = {
    "discussion": 0.36,
    "assignment": 0.36,
    "exercise": 0.14,
    "quiz": 0.14
}

#discussion grades
num_discussion = int(input("how many discussion posts were assigned in the course?"))
discussion_points = num_discussion * 6
#creates empty list to store pointsa
earned_discussion_points = []

print("We will start by entering your points earned on each assignment in the course. We will start with your discussion posts. They are worth 6 points each")


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
    if len(earned_discussion_points) >= num_discussion:  #stop collecting values once we have the amount of discussion posts there were
        break
    earned_discussion_points.append(float(discuss))
total_earned_discussion_points = sum(earned_discussion_points)


#assignment grades
num_assignment = int(input("how many weekly assignments were assigned in the course?"))
assignment_points = num_assignment * 6
    # creates empty list to store the points
earned_assignment_points = []

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
    if len(earned_assignment_points) >= num_assignment:  #stop collecting values once we have the number of assignments there were
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
print(f"the average for the w3 quiz was {earned_quiz}%, with points totaling to {earned_quiz_points} out of 14.")
print(f"the average for the w3 exercises was {earned_exercise}%, with points totaling to {earned_exercise_points} out of 14.")

# multiply each percentage by its cooresponding category weight

discussion = deliverable_weight["discussion"] * float(earned_discussion)
assignment = deliverable_weight["assignment"] * float(earned_assignment)
exercise = deliverable_weight["exercise"] * float(earned_exercise)
quiz = deliverable_weight["quiz"] * float(earned_quiz)

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