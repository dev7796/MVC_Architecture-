import pandas as pd
import numpy as np
df = pd.DataFrame({
     'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
     'col2': [2, 1, 9, 8, 7, 4],
  'col3': [0, 1, 9, 4, 2, 3]})
print(df.sort_values(by=['col1']))