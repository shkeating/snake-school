# grade calculator
# # #
# takes in inputs from the user and calculates 
# the final course grade using the weights of 
# each type of assignment

# variable initalization

# assignment type weights
weight_discussion = 0.36
weight_assignment = 0.36
weight_exercise = 0.14
weight_quiz = 0.14

#assignment grades
assignment_points = 36
    # creates empty list to store the points
earned_assignment_points = []

    #assignment point collection loop so we aren't here all day
    for i in range(1, 7):
       

#discussion grades
discussion_points = 36
earned_discussion_points = 

#w3 exercise grade
exercise_points = 14
earned_exercise_points = input('please enter points earned on w3 exercises, up to 14 points')

#w3 quiz grade
quiz_points = 14
earned_quiz_points = input('please enter points earned on w3 quiz, up to 14 points')


# earned grades inputs
earned_discussion = input('please enter a numerical percentage grade from 0-100 of discussion posts: ')
earned_assignment = input('please enter a numerical percentage grade from 0-100 of weekly assignments: ')
earned_exercise = earned_exercise_points / exercise_points * 100
earned_quiz = earned_quiz_points / quiz_points * 100

# multiply each percentage by its cooresponding category weight

discussion = weight_discussion * float(earned_discussion)
assignment = weight_assignment * float(earned_assignment)
exercise = weight_exercise * float(earned_exercise)
quiz = weight_quiz * float(earned_quiz)

# sum the categories to get output of numerical grade earned
grade = discussion + assignment + exercise + quiz
# future enhancement: add in the corresponding letter grade to the calculated number

#print final grade
print('Your final grade calculates to ' + str(grade) + '%.')