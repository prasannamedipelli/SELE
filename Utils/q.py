import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data=[
    [10,5,4],
    [3,12,8],
    [12,15,3]
]
df=pd.DataFrame(data, columns=["Chrome","Firefox","Edge"], index=["Monday","Tuesday","Wednesday"])
sns.heatmap(df, annot=True)
plt.title("Browser usage")
plt.show()