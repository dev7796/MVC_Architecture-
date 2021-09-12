import pandas as pd
def cal_percent(ls1,ls2):
    result=[]
    for i in range(len(ls1)):
        result.append(ls2[i]/ls1[i]*100)
    return result
ls,ls1,ls2=[],[],[]
df = pd.read_excel('IPL.xls')
data=df.groupby('Winner')
Unique_data=df['Winner'].unique()
ls.append(Unique_data[0])
ls.append(Unique_data[1])
ls.append(Unique_data[6])
ls.append(Unique_data[7])
dict_BF={}
dict_total_wins={}
for i in range(len(ls)):
    df1 = df[df['Winner'] == ls[i]].set_index('Match_Number')
    dict_total_wins[ls[i]] = df1[(df1['Winner'] == ls[i])].count().max()
    dict_BF[ls[i]] = df1[(df1['Winning_Team'] == "FirstBatting")].count().max()
for v in dict_total_wins.values():
    ls1.append(v)
for v in dict_BF.values():
    ls2.append(v)

Total=cal_percent(ls1,ls2)
MatchData=pd.DataFrame({'Teams': ls,
                        'Percent won batting first ': Total}).set_index('Teams')
print(MatchData)
df2=MatchData.to_csv('file1')


