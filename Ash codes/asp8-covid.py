import pandas as pd
import matplotlib.pyplot as plt

cases = [5,7,10,15,18,20,25,30,28,35,40,42,38,50,60,58,62,65,70,72,75,80,85,90,100,105,95,92,98,110]
df = pd.Series(cases, index=pd.date_range("2020-03-01", periods=30))

df.plot(alpha=0.5, label='Daily')
df.rolling(7).mean().plot(label='7-Day Avg', linewidth=2)

plt.title("COVID-19 Trend")
plt.ylabel("Cases")
plt.legend()
plt.show()
