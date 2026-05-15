import seaborn as sns
import matplotlib.pyplot as plt

days =[1,2,3,4,5]
traffic =[150,300,500,200,100]

sns.barplot(x=days, y=traffic)
plt.title("Website traffic")
plt.show()