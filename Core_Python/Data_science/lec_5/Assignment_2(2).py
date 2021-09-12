import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Data20.csv')
df1 = pd.read_csv('Data21.csv')
df.plot(x='City',y=['Hereditary','Auto-Immune','Infectious','Natural_Cause','Contamination'],kind='bar')
plt.ylabel("Number of cases")
df1.plot(x='Type Of Disease',y='Count',kind='bar')
plt.show()
