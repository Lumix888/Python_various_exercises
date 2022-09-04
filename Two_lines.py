import matplotlib.pyplot as plt

X1 = [1,2,3]
Y1 = [1,6,8]
X2 = [4,7,9]
Y2 = [9,3,4]

plt.plot (X1, Y1, 'bo-', X2, Y2, 'r*:')

plt.title ("Two lines")

plt.legend (['line1', 'line2'])

plt.show ()
