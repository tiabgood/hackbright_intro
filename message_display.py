#Both of the below work - I was just trying different ways.


# message, num = input ('Please put a message in quotes, a comma, and then the number of times you would like it to print. ')

# for index in range (0, num):
# 	print message


question = raw_input ("Please put a message and the number of times you want it to be printed. ")

answers = question.split(' ')

num = int(answers[-1])

for index in range (0, num):
	print ' '.join(answers[0:-1])
	print ("\n\r")


