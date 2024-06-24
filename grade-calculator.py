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

# earned grades inputs
earned_discussion = input('please enter a numerical percentage grade from 0-100 of discussion posts ')
earned_assignment = input('please enter a numerical percentage grade from 0-100 of weekly assignments ')
earned_exercise = input('please enter a numerical percentage grade from 0-100 of w3 exercises ')
earned_quiz = input('please enter a numerical percentage grade from 0-100 of w3 quizzes ')

# multiply each percentage by its cooresponding category weight

discussion = weight_discussion * float(earned_discussion)
assignment = weight_assignment * float(earned_assignment)
exercise = weight_exercise * float(earned_exercise)
quiz = weight_quiz * float(earned_quiz)

# sum the categories to get output of numerical grade earned
grade = discussion + assignment + exercise + quiz

#print final grade
print('your final grade calculates to' + grade + '.')