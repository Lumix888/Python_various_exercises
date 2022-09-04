import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_excel(r'Number_and_Price.xls')

data['New_Col'] = data['Number'] * data['Price']

print(data.New_Col)

group = data.groupby('Price') 

print(group.get_group(1000))

x = data.Number
y = data.Price

stats = linregress(x, y)

m = stats.slope
b = stats.intercept

plt.figure(figsize = (10,10))

plt.scatter(x, y, marker = 'x')

plt.plot(x, m * x + b, color = "red", linewidth=3)

plt.xlabel("Height (m)", fontsize = 20)
plt.ylabel("Latitude", fontsize = 20)

plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)

plt.savefig("linear_reg_number_price.png")

