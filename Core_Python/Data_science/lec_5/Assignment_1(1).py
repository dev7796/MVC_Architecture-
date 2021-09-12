import pandas as pd
import numpy as np



#Maximum admissions amongst all university
data0 = pd.read_excel('University.xlsx')
data=data0.dropna()
df=pd.DataFrame(data,columns=['University'])
result={}
Unique_data=df['University'].unique()
for i in Unique_data:
    result[i]=df[df['University']==i].count().max()
v = list(result.values())
k = list(result.keys())
max_venue=k[v.index(max(v))]
max_venue_value=max(v)
d={"University":[max_venue],
   "Count":[max_venue_value]}
df1=pd.DataFrame(d)
df1.to_csv('Data1.csv')


#countng year wise University admissions
df1 = pd.read_excel('University.xlsx')
df=df1.dropna()
ls=[]
data=df.groupby('Passing Year')
Unique_data=df['Passing Year'].unique()
for i in Unique_data:
    ls.append(i)
dict_Cornell={}
dict_Pennsylvania={}
dict_Columbia={}
for i in range(len(ls)):
    dict_Cornell[ls[i]]=df[(df['Passing Year']==ls[i]) & (df['University']=='Cornell Univerisity')].count().max()
    dict_Pennsylvania[ls[i]]=df[(df['Passing Year']==ls[i]) & (df['University']=='University of Pennsylvania')].count().max()
    dict_Columbia[ls[i]]=df[(df['Passing Year']==ls[i]) & (df['University']=='Columbia Univerisity')].count().max()
bf_value = list(dict_Cornell.values())
ch_value= list(dict_Pennsylvania.values())
mt_value = list(dict_Columbia.values())
MatchData=pd.DataFrame({'Year':df['Passing Year'].unique().astype(int),
                    'Cornell University':bf_value,
                    'University of Pennsylvania':ch_value,
                    'Columbia University':mt_value
                        })
MatchData.to_csv("Data0.csv")

#percent of admission each university recieved with GRE>310 and Toefl>100 each year

def cal_percent(ls1,ls2):
    result=[]
    for i in range(len(ls1)):
        result.append(ls2[i]/ls1[i]*100)
    return result
ls,ls1,ls2=[],[],[]
df1 = pd.read_excel('University.xlsx')
df=df1.dropna()
data=df.groupby('University')
Unique_data=df['University'].unique()
dict_university={}
dict_total_admits_conditions={}
for i in range(len(Unique_data)):
    df2 = df[df['University'] == Unique_data[i]]
    dict_university[Unique_data[i]] = df2[(df2['University'] == Unique_data[i])].count().max()
    dict_total_admits_conditions[Unique_data[i]] = df2[(df2['GRE'] >=290) & (df2['TOEFL'] >= 100) & (df2['GPA'] >= 7.0)].count().max()
for v in dict_total_admits_conditions.values():
    ls1.append(v)
for v in dict_university.values():
    ls2.append(v)
Total=cal_percent(ls2,ls1)
MatchData=pd.DataFrame({'Teams': Unique_data,
                        'Percent Admits per year': Total})
df2=MatchData.to_csv('Data2.csv')




