# Define a function calc_max that takes a list of four grades (of type float) as a parameter and returns the max grade in that list.
# Outside the function, ask the user to enter four grades and save them in a list grades_list.
# Call the function calc_max and pass grades_list as an argument.
# Print the returned value from the function calc_max

def bigger (num1, num2):
	if num1>num2:
		return num1
	return num2

def calc_max (grades):
	return bigger (bigger(grades[0],grades[1]), bigger(grades[2],grades[3]))

grades_list = []
for number in range (0,4):
    grades_list.append(float(raw_input("What is your number %s grade? " %str(number+1))))
    
print calc_max (grades_list)

