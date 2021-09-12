#Q.3

import pandas as pd
data = pd.read_excel('IPL.xls')
'''df = pd.DataFrame(data, columns= ['Bat_First_Run_Rate'])
lst=df['Bat_First_Run_Rate'].to_list()
df1 = pd.DataFrame(data, columns= ['Bat_First_Run_Rate','Team_Batting_First','Bat_First_Runs_Scored','Bat_First_Overs_Consumed'])
rslt_df=df1[df1['Bat_First_Run_Rate']==df1['Bat_First_Run_Rate'].max()]
for i in (rslt_df['Bat_First_Run_Rate']):
    Bat_First_Run_Rate=i
for i in (rslt_df['Team_Batting_First']):
    Team_Batting_First=i
for i in (rslt_df['Bat_First_Runs_Scored']):
    Bat_First_Runs_Scored=i
for i in (rslt_df['Bat_First_Overs_Consumed']):
    Bat_First_Overs_Consumed=i
d={"":[rslt_df['Team_Batting_First'],Team_Batting_First,Bat_First_Runs_Scored,Bat_First_Overs_Consumed]}
final=pd.DataFrame(d,index=['Bat_First_Run_Rate','Team_Batting_First','Bat_First_Runs_Scored','Bat_First_Overs_Consumed'])
print(final)

#use loc function and try'''

Highest_rr = data['Bat_First_Run_Rate'].max()
match_no=int(data[data['Bat_First_Run_Rate'] == Highest_rr].index.values)
table3 = pd.Series([match_no,
                    data.loc[match_no,'Team_Batting_First'],
                    data.loc[match_no,'Bat_First_Runs_Scored'],
                    data.loc[match_no,'Bat_First_Overs_Consumed']],
                   ['Match No.','Team_Batting_First','Bat_First_Runs_Scored','Bat_First_Overs_Consumed'])
print(table3)
