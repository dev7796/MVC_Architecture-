import pandas as pd
ls=[]
df = pd.read_excel('Project_Analysis.xlsx')
df1 = pd.read_excel('Project_Analysis_DISTRICT.xlsx')
df3=pd.merge(df,df1,on='State  Code')
df3.to_excel('Project_Analysis_FINAL.xlsx')