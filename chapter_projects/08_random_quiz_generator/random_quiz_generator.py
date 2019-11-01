#! python3
# random_quiz_generator.py - Creates quizzes with questions and answers in 
# random order, along with the answer key

import random

# The quiz data. Keys are states and values are their capitals

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files

for quizNum in range(35):
	# Open (create) quiz text files named capitalsquiz<N>.txt or capitalsquiz_answers<N>.txt
	# %s appears to be a generic placeholder that will be filled by the following value
	# defined
	quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

	# The below creates a quiz header for the student to fill in their details
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
	quizFile.write('\n\n')

	# A randomized list of US states is created with random.shuffle() function
	# which randomly reorders the values in any list passed to it
	states = list(capitals.keys())
	random.shuffle(states)

	# Creating the answer options, a lot going on here that's new, so I'll comment
	# more heavily below
	for questionNum in range(50):
		# In this case, the variable states contains a randomized list of only the
		# keys from the capitals dictionary. questionNum, the initializer in the loop,
		# is used to define an index for searching the states list value. The capitals
		# dictionary is then searched using the key (a state name), to find its
		# corresponding value (capital city)
		correctAnswer = capitals[states[questionNum]]
		# To get the wrong answer, a list of all values in the capitals dictionary is
		# created, then the CORRECT answer is deleted.  wrongAnswers.index(correctAnswer)
		# will return the correct answers current index value, which is then passed as the
		# index on the delete statement for the wrongAnswers list value
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		# wrongAnswers is then updated to contain a random sample of 3 of the wrong 
		# answers
		wrongAnswers = random.sample(wrongAnswers, 3)
		# A new variable, answerOptions, then comines the single correct answer 
		# with the three incorrect options
		answerOptions = wrongAnswers + [correctAnswer]
		# The answer options are then further shuffled (so the correct answer 
		# doesn't always show in the same slot for example)
		random.shuffle(answerOptions)
		# Write each question in teh quizFile, then...
		quizFile.write('%s. What is the capital of %s\n' % (questionNum + 1, states[questionNum]))
		# This loop goes through integers 0 to 3 and will write the answer 
		# options from the answerOptions list
		for i in range(4):
			# The expression 'ABCD'[i] treats the string as an array and will
			# evaluate to A, B, C, D on each loop
			quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
			quizFile.write('\n')
			# answerOptions.index(correctAnswer) will return the index of the
			# correct answer and the corresponding letter will be written to
			# the answer key!
			answerKeyFile.write('%s. %s\n' % (questionNum + 1, 
				'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()