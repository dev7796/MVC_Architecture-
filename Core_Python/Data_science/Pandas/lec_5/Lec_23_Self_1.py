from venv import create

import pandas as pd
ls,ls1=[],[]
df1={}
data = pd.read_excel('IPL.xls')
data0=pd.DataFrame(data,columns=('Match_Number','Team_Batting_Second','Team_Batting_First','Date'))
data1=pd.DataFrame(data,columns=('Bat_First_Runs_Scored','Bat_Second_15_ov_score')).astype(float)
df=data.groupby('Team_Batting_Second')
Unique_data=df['Team_Batting_Second'].unique()

'''for i in Unique_data:
    ls.append(i[0])
for j in ls:
    #1. Unique teams won match how many times with wintype = run and win margin>5077 and batting first

    df1[j]=data[(data['Winner']==j) & (data['Winning_Team']=='FirstBatting') & (data['Winning_Margin'] >= 30) & (data['Win_Type'] == 'run')].count().max()

answer=[*df1.values()]
data0=pd.DataFrame(columns=ls)
print(data0.append(df1,ignore_index=True))'''

'''    #2. Bat_Second_10_ov_Req_RR<5 Bat_Second_15_ov_wkts_lost>5 but scored more than 30 in last 5 overs and won
data_frame_diff=data1.diff(axis=1)
df1=data[(data['Bat_Second_15_ov_wkts_lost']>4) & (data['Winning_Team']=='Chasing') & (data['Bat_Second_10_ov_Req_RR'] < 7) & (data_frame_diff['Bat_Second_15_ov_score'] >= -30)].index.tolist()
final=data0.iloc[df1]
print(final)'''

#3. finding correlations between columns
#we can create
#print(data.corr(method='pearson'))

'''#4. no of match tied by each team
for i in Unique_data:
    ls.append(i[0])
for j in ls:
    df1[j] = data[(((data['Team_Batting_First'] == j) | (data['Team_Batting_Second'] == j)) & (data['Winner'] == 'Match tied'))].count().max()
data_list=list(df1.items())
df2 = pd.DataFrame(data_list)
df2.columns=['Teams','Total number.']
print(df2)'''

# 5. wicket lost in last 5 overs is less than 1 but still lost the match with batting first
df1=data[['Bat_Second_20_ov_wkts_lost']]
df2=df1.fillna(0)
df3=data[['Bat_Second_15_ov_wkts_lost']]
df4=df3.fillna(0)
df5=pd.concat([df2,df4],axis=1)
data_frame_diff=df5.diff(axis=1)
df1=data[(data['Winning_Team']=='Chasing')  & (data_frame_diff['Bat_Second_15_ov_wkts_lost'] <= 1)].index.tolist()
