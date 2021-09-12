import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''df = pd.read_excel('world 2.xlsx').fillna(0)
ls=[]
data=df.groupby('Country')
Unique_data=df['Country'].unique()
for i in Unique_data[1:]:
    ls.append(i)
ls.pop()
# it provides a list of countries with cases more than 50000 and total cases
dict_Total_cases={}
Tc_value=[]
for i in range(len(ls)):
    dict_Total_cases[ls[i]]=df[(df['Country']==ls[i]) & (df['Total Cases'] >= 50000) & (df['Total Deaths'] <= 10000)].index.tolist()
for i in dict_Total_cases.values():
    for j in i:
        Tc_value.append(j)
df1=df.iloc[Tc_value,[0,1,3,5]]
print(df1)
df1.plot(x='Country',y=['Total Cases','Total Deaths','Total Recovered'],kind='bar',title='List of countries with cases > 50000 total cases and Deaths < 10000')
plt.show()'''



# top 5 countries with max active cases
df = pd.read_excel('world 2.xlsx').fillna(0)
df1= df[['Country','Active Cases',"New Cases","Tot Cases/ 1M pop","Total Cases"]]
df1.drop(df.tail(1).index,inplace=True)
df1.drop(df.head(1).index,inplace=True)
df1=df1.sort_values(by=["Active Cases"],ascending=False)
df2=df1.head(8)
print(df2)
df2.plot(x='Country',y=['Active Cases',"New Cases",'Total Cases'],kind='line',title='Top 8 countries with max active cases as compared to New Cases',marker='o')
plt.show()


# top 5 countries with max recovered and least new cases
'''df = pd.read_excel('world 2.xlsx').fillna(0)
df1= df[['Country','Total Recovered',"New Cases","Population","Total Cases","Total Deaths"]]
df1.drop(df.tail(1).index,inplace=True)
df1.drop(df.head(1).index,inplace=True)
df1=df1.sort_values(by=['New Cases',"Total Recovered"],ascending=(True,False))
df2=df1.head(8)
df2.plot(x='Country',y=['New Cases',"Total Recovered","Total Cases","Total Deaths"],kind='bar',title='Top 8 countries with max recovered and least new cases')
plt.show()'''



# countries with active more than recovered

'''df = pd.read_excel('world 2.xlsx').fillna(0)
ls=[]
data=df.groupby('Country')
Unique_data=df['Country'].unique()
for i in Unique_data[1:]:
    ls.append(i)
ls.pop()
dict_Total_cases={}
Tc_value=[]
for i in range(len(ls)):
    dict_Total_cases[ls[i]]=df[(df['Country']==ls[i]) & (df['Active Cases'] > df['Total Recovered'])].index.tolist()
for i in dict_Total_cases.values():
    for j in i:
        Tc_value.append(j)
df1=df.iloc[Tc_value,[0,1,5,6]]
df2=df1.head(8)
df2.plot(x='Country',y=['Total Cases',"Total Recovered","Active Cases"],kind='bar',title='Top 8 countries with Active Cases are more than Recovered Cases')
plt.show()'''



# countries ratio of total tests to pupolation and total deaths to population

'''def cal_percent(ls1,ls2):
    result=[]
    for i in range(len(ls1)):
        if ls2[i]==0:
            result.append(0)
        else:
            result.append(ls1[i]/ls2[i]*10000)
    my_formatted_list = ['%.2f' % elem for elem in result]
    return my_formatted_list
def cal_percent1(ls1,ls2):
    result=[]
    for i in range(len(ls1)):
        if ls2[i]==0:
            result.append(0)
        else:
            result.append(ls1[i]/ls2[i]*100)
    my_formatted_list = ['%.2f' % elem for elem in result]
    return my_formatted_list
ls,ls1,ls2,ls3=[],[],[],[]
df = pd.read_excel('world 2.xlsx').fillna(0)
data=df.groupby('Country')
Unique_data=df['Country'].unique()
for i in Unique_data[1:10]:
    ls.append(i)
ls.pop()
dict_Population={}
dict_total_deaths={}
dict_tests={}
for i in range(len(ls)):
    #df1 = df[df['Winner'] == ls[i]].set_index('')
    dict_total_deaths[ls[i]] = int(df.iloc[i+1,3])
    dict_Population[ls[i]] = int(df.iloc[i+1,12])
    dict_tests[ls[i]] = int(df.iloc[i+1,10])
for v in dict_total_deaths.values():
    ls1.append(v)
for v in dict_Population.values():
    ls2.append(v)
for v in dict_tests.values():
    ls3.append(v)
Total=cal_percent(ls1,ls2)
Tests = cal_percent1(ls3,ls2)
MatchData=pd.DataFrame({'Country': ls,
                        'Rate of death to population': Total,
                        'Rate of tests to population': Tests})
dict={'Rate of death to population': float,
      'Rate of tests to population' : float}
MatchData = MatchData.astype(dict)
MatchData.plot(x='Country',y=['Rate of death to population','Rate of tests to population'],kind='bar',title='Countries ratio of total tests to pupolation and total deaths to population')
plt.show()'''


