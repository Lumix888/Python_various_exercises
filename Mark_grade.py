grade = int(input("To get the grade insert the mark: "))

if grade <= 100 and grade >= 90:
    print ("The grade is A+")
if grade <= 89 and grade >= 80:
    print ("The grade is A")
if grade <= 79 and grade >= 70:
    print ("The grade is B")
if grade <= 69 and grade >= 60:
    print ("The grade is C")
if grade <= 59 and grade >= 50:
    print ("The grade is D")
if grade < 50 and grade >= 0:
    print ("The grade is Fail")
else:
    print ("the mark inserted is not valid, please insert an integer betwee 0 and 100")
    