import pandas as pd
import numpy as np



#Count of maximum kind of diseases amongst all
data0 = pd.read_excel('BloodGroup.xlsx')
data=data0.dropna()
df=pd.DataFrame(data,columns=['Type Of Disease'])
result={}
Unique_data=df['Type Of Disease'].unique()
for i in Unique_data:
    result[i]=df[df['Type Of Disease']==i].count().max()
v = list(result.values())
k = list(result.keys())
max_venue=k[v.index(max(v))]
max_venue_value=max(v)
d={"Type Of Disease":[max_venue],
   "Count":[max_venue_value]}
df1=pd.DataFrame(d)
df1.to_csv('Data21.csv')




#countng disease city wise
df1 = pd.read_excel('BloodGroup.xlsx')
df=df1.dropna()
ls=[]
data=df.groupby('Places')
Unique_data=df['Places'].unique()
for i in Unique_data:
    ls.append(i)
#'Rajkot','Vadodra','Surat','Gandhinagar','Ahmedabad','Anand','Bhuj','Jamnagar'
# Autoimmune Diseases','Allergies & Asthma','Cancer','Celiac Disease','Crohns & Colitis','Heart Disease','Infectious Diseases','Liver Disease'
# 'Hereditary','Auto-Immune','Infectious','Natural-Cause','Contamination'
dict_Hereditary={}
dict_Auto_Immune={}
dict_Infectious={}
dict_Natural_Cause={}
dict_Contamination={}
for i in range(len(ls)):
    dict_Hereditary[ls[i]]=df[(df['Places']==ls[i]) & (df['Cause Of Disease']=='Hereditary')].count().max()
    dict_Auto_Immune[ls[i]]=df[(df['Places']==ls[i]) & (df['Cause Of Disease']=='Auto-Immune')].count().max()
    dict_Infectious[ls[i]]=df[(df['Places']==ls[i]) & (df['Cause Of Disease']=='Infectious')].count().max()
    dict_Natural_Cause[ls[i]] = df[(df['Places'] == ls[i]) & (df['Cause Of Disease'] == 'Natural-Cause')].count().max()
    dict_Contamination[ls[i]] = df[(df['Places'] == ls[i]) & (df['Cause Of Disease'] == 'Contamination')].count().max()
h_value = list(dict_Hereditary.values())
ai_value= list(dict_Auto_Immune.values())
i_value = list(dict_Infectious.values())
nc_value = list(dict_Natural_Cause.values())
c_value = list(dict_Contamination.values())
MatchData=pd.DataFrame({'City':ls,
                    'Hereditary':h_value,
                    'Auto-Immune':ai_value,
                    'Infectious':i_value,
                    'Natural_Cause':nc_value,
                    'Contamination':c_value
                        })
print(MatchData)
MatchData.to_csv("Data20.csv")





