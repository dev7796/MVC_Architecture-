'''import pandas as pd
import pymysql as sql
import numpy as np
from sqlalchemy import create_engine

df = pd.DataFrame({'employers_ID':[12,13],
                   'username':["lalal",'jigal'],
                   'password':['jingala','kakak'],
                   'time':['34349','56'],
                   'age':[22,24]}).set_index('employers_ID')

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user='root',
                               pw='gladiators',
                               db='employee'))
# cursor = connection.cursor()
# df2 = pd.read_sql('SELECT * FROM rough',connection)

# cursor = connection.cursor()
df.to_sql('employers1', con=engine, if_exists='append')
# cursor.execute(df1)
# connection.commit()'''

GEEK = [6, 0, 4, 1]
k=len(GEEK)
for i in range(k,10):
    GEEK.append(0)
print(GEEK)

