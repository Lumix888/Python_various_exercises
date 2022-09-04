number = int(input('Write a natural number: '))

i = number

while i > 0:
    if (number % i) == 0:
        print (int(number / i))
    i = i - 1
