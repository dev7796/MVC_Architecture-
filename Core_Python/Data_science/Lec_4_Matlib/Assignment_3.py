import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('file1',index_col='Teams')
df1 = pd.read_csv('file2')
df1.plot(x='Year',y=['Total No of matches','Number of matches Team Batting First Won','Number of matches team Chasing Won','Number of times Match Tied'],kind='line')
df.plot(y='Percent won batting first ',kind='pie')
plt.show()



