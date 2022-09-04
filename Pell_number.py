def pell(n):
    a = 0
    b = 1
    while n > 0:
        print (a)
        a, b = b, b * 2 + a
        n = n - 1

pell(int(input("Write the Nth pell number to be print: ")))
