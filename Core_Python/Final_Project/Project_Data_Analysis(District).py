import pandas as pd
ls=[]
df = pd.read_excel('A-1_NO_OF_VILLAGES_TOWNS_HOUSEHOLDS_POPULATION_AND_AREA.xlsx').dropna()
data = pd.DataFrame(df)
df1 = pd.DataFrame(columns=['District  Code'])
unique_state = df[df['India/ State/ Union Territory/ District/ Sub-district'] == 'DISTRICT']['Name'].unique()
data_set={}
for i in unique_state:

    data_set[i] = df[(df['Name']==i)& (df['India/ State/ Union Territory/ District/ Sub-district'] == 'DISTRICT')&((df['Total/Rural/Urban']=='Rural') | (df['Total/Rural/Urban']=='Urban'))]
    df1=pd.concat(data_set)

#df1 = df1.drop(df1.columns[0], axis=1)

print(df1)
df1.to_excel('Project_Analysis_DISTRICT.xlsx')