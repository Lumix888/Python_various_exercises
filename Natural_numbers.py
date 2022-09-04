Number = int(input('Write a natural number: '))

sum = 0

for x in range(0, Number + 1, +1):
    sum = sum + x
print ("The natural numebers up to the given integer add up to:" ,sum)
