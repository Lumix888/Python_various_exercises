cap = int(input("Write the cap number to get the Fibonacci series: "))

a = 0
b = 1

while b <= cap:
    a, b = b, a + b
    print (a)
    