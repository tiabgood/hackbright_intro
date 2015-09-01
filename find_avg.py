def find_average (num1, num2, num3):
    if (type(num1)==int or type(num1)==float) and (type(num2)==int or type(num2)==float) and (type(num3)==int or type(num3)==float):
            average = float((num1+num2+num3)/3)
            return "Average is", average
    else:
        return "Sorry the input(s) are invalid"


print find_average(3,4,4)

print find_average(1,2,3)

print find_average('6', 8, 7)

print find_average(2, 9,'hi')

print find_average(2, '9','hi')