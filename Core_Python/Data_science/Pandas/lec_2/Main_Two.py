import pandas as pd
import pymysql
from sqlalchemy import create_engine

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='pythondb',
    cursorclass=pymysql.cursors.DictCursor
)

df = pd.read_sql('select * from loginmaster', connection)

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="root",
                               db="pythondb"))
df.to_sql(con=connection, name='loginmaster', if_exists='replace')

print("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root", pw="root", db="pythondb"))
