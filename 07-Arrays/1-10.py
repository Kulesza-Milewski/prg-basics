###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
   if answer == True:
      correct_answers = correct_answers + 1

# calculates the number of incorrect answers
incorrect_answers = question_number - correct_answers

# calculates the percentage of correct answers
procentage = (100/question_number)*correct_answers

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Procentage of correct answers:', round(procentage, 2), '%')