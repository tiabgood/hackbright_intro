def find_average (num1, num2, num3):
    if type(num1)!=int or type(num1)!=float:
        return "Sorry the input(s) are invalid"
    elif type(num2)!=int or type(num2)!=float:
        return "Sorry the input(s) are invalid"
    elif type(num2)!=int or type(num2)!=float:
        return "Sorry the input(s) are invalid"
    else:
            average = float((num1+num2+num3)/3)
            return "Average is", average


print find_average(3,4,4)

print find_average(1,2,3)

print find_average('6', 8, 7)

print find_average(2, 9,'hi')

print find_average(2, '9','hi')