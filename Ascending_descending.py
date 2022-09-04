def addnum():
    if len(lst) <= 4:
        a = int(input("Enter an int number: "))
        lst.append(a)
        addnum()

lst = []

addnum()

print("Ascending order: ", sorted(lst))
print("Descending order: ", sorted(lst, reverse=True))
