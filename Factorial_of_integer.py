Number = int(input('Write a natural number: '))

i = Number
Fact = Number

for i in range(Number, 1, - 1):
    Fact = Fact * (i - 1)
print (Number, "factorial is:", Fact)
