import pandas as pd
ls,ls1=[],[]
df = pd.read_excel('IPL.xls')
data=df.groupby('Year')
Unique_data=df['Year'].unique()
for i in Unique_data:
    ls.append(i)
dict_final={}
for i in range(len(ls)):
    df1 = df[df['Year'] == ls[i]].set_index('Match_Number')
    dict_final[ls[i]] = df1[(df1['Balls_Remaining'] <= 3) | (df1['Winning_Team'] == 'Match Tied') | ((df1['Winning_Team']=='FirstBatting') & ((df1['Win_Type'] == 'wicket') & (df1['Winning_Margin'] <= 1))) | ((df1['Winning_Team']=='Chasing') & ((df1['Win_Type']=='run')) & ((df1['Winning_Margin'] <= 5)))].index.tolist()

for k,v in dict_final.items():
    ls1.append(len(v))
MatchData=pd.DataFrame({'Year':df['Year'].unique(),
                    'Total No of matches': ls1})
print(MatchData)







'''for k,v in dict_final.items():
    ls.append(v.count())
print(ls)
mt_value = list(dict_tied.values())
Wr_value= list(dict_chasing_Wickets.values())

MatchData=pd.DataFrame({'Year':df['Year'].unique(),
                    'Number of matches':mt_value,
                    'Balls remianing':Wr_value
                        })
print(MatchData)'''
