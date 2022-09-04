def mean(x):
    m = sum(x) / len(x)
    return m

def addnum():
    a = float(input("Please enter the numbers,\nany negative number will terminate the input: "))
    if a >= 0:    
        lst.append(a)
        addnum()

lst = []

addnum()

print("The positive numebrs are: ", lst)
print("The sum of the positive numebers is: ", sum(lst))
print("The average of the positive numbers is: ", mean(lst))
print("The maximum is: ", max(lst))
print("The minimum is: ", min(lst))
