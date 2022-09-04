n = int(input("Write the Nth pell number to be print: "))

def pell(n):
    if n <=2:
        return n
    else:
        return(pell(n-1)*2 + pell(n-2))

for i in range(n + 1):
    print(pell(i))
    