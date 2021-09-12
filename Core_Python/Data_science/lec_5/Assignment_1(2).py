import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Data0.csv')
df1 = pd.read_csv('Data2.csv')
df2 = pd.read_csv('Data1.csv')
df.plot(x='Year',y=['Cornell University','University of Pennsylvania','Columbia University'],kind='bar')
df1.plot(x='Teams',y='Percent Admits per year',kind='bar',color=(0.2, 0.4, 0.6, 0.6))
df2.plot(x='University',y='Count',kind='bar')
plt.show()
