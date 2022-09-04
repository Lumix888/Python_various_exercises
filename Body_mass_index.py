def BMI(x):
    if x < 18.5:
        print("Underweight")
    else:
        if  x <25:
            print("Normal weight")
        else:
            if x < 30:
                print("Overweight") 
            else:
                print("Obesity")
        
BMI(int(input('Write BMI: ')))
