import pandas as pd
ls=[]
df = pd.read_excel('A-1_NO_OF_VILLAGES_TOWNS_HOUSEHOLDS_POPULATION_AND_AREA.xlsx').dropna()
data = pd.DataFrame(df)
df1 = pd.DataFrame(columns=['State  Code'])
unique_state = df[df['India/ State/ Union Territory/ District/ Sub-district'] == 'STATE']['Name'].unique()
data_set={}
for i in unique_state:

    data_set[i] = df[(df['Name']==i)& ((df['Total/Rural/Urban']=='Rural') | (df['Total/Rural/Urban']=='Urban'))]
    df1=pd.concat(data_set)
print(df1)
df1.to_excel('Project_Analysis.xlsx')

#data.to_excel('Project_Analysis.xlsx')