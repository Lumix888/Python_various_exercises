import numpy as np 
import matplotlib.pyplot as plt 
  
cars = ['Comedy', 'Action', 'Romance', 'Drama', 'SciFi']  
data = [4, 5, 6, 1, 4] 
explode = (0.1, 0.1, 0.1, 0.1, 0.1) 
colors = ( "yellow", "orange", "red", "blue", "green")   
wp = { 'linewidth' : 3, 'edgecolor' : "black" } 
  
def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n({:d} votes)".format(pct, absolute) 
  
fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data, autopct = lambda pct: func(pct, data), explode = explode, labels = cars, shadow = True, colors = colors, startangle = 90, wedgeprops = wp, textprops = dict(color ="black")) 

ax.legend(wedges, cars, title ="Type of movie", loc ="center", bbox_to_anchor =(1, 0, 0.5, 1)) 
  
plt.setp(autotexts, size = 8, weight ="bold")
 
ax.set_title("Table: Favourite Type of Movie") 

plt.show()
