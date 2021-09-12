import pandas as pd
ls,ls1=[],[]
data = pd.read_excel('IPL.xls')
data0=pd.DataFrame(data,columns=('Match_Number','Team_Batting_Second','Team_Batting_First','Date'))
data1=pd.DataFrame(data,columns=('Bat_First_15_ov_score','Bat_First_20_ov_score')).astype(float)
data_frame_diff=data1.diff(axis=1)
df=data.index.tolist()
dict_final={}
df1=data[(data['Bat_First_15_ov_wkts_lost'] == 2) & (data_frame_diff['Bat_First_20_ov_score'] < 25)].index.tolist()
final=data0.iloc[df1]
print(final)
