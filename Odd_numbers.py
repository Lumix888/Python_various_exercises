number1 = int(input('Start of the range for odd numbers: '))
number2 = int(input('End of the range for odd numbers: '))

while number1<= number2:
    if (number1 % 2) == 1:
        print (number1)
    number1 = number1 + 1
