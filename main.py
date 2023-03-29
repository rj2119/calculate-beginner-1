number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
if (number_1*number_2) <= 1000:
    mul = number_1 * number_2
    print("The result is {}".format(mul))
else:
    add = number_1 + number_2
    print("The result is {}".format(add))