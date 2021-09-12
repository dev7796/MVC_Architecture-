import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
ls=[]
df = pd.read_excel('IPL.xls')
data=df.groupby('Year')

Unique_data=df['Year'].unique()
for i in Unique_data:
    ls.append(i)
dict_matches={}
dict_firstbat={}
dict_chasing={}
dict_tied={}
for i in range(len(ls)):
    dict_matches[ls[i]]= df[(df['Year']==ls[i])].count().max()
    dict_firstbat[ls[i]]=df[(df['Year']==ls[i]) & (df['Winning_Team']=='FirstBatting')].count().max()
    dict_chasing[ls[i]]=df[(df['Year']==ls[i]) & (df['Winning_Team']=='Chasing')].count().max()
    dict_tied[ls[i]]=df[(df['Year']==ls[i]) & (df['Winning_Team']=='Match Tied')].count().max()
tm_value= list(dict_matches.values())
bf_value = list(dict_firstbat.values())
ch_value= list(dict_chasing.values())
mt_value = list(dict_tied.values())

MatchData=pd.DataFrame({'Year':df['Year'].unique(),
                    'Total No of matches': tm_value,
                    'Number of matches Team Batting First Won':bf_value,
                    'Number of matches team Chasing Won':ch_value,
                    'Number of times Match Tied':mt_value

                        })
print(MatchData['Number of matches Team Batting First Won'],MatchData['Number of matches team Chasing Won'])

plt.ylabel('Different values')
plt.xlabel('Years')

t = np.arange(ls[0], ls[-1]+1, 1)
plt.plot(t, tm_value, '--bo',t,bf_value,'--go',t,ch_value,'--ro',t,mt_value,'--ko')
'''markers_on=[1,2,3]
plt.plot(t, tm_value, 'b--',t,bf_value,'g--',t,ch_value,'r--',t,mt_value,'k--',markevery=markers_on)'''
plt.annotate('Total No. of matches', xy=(2008, 58), xytext=(2008, 62),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
#plt.plot(range(10), linestyle='--', marker='o', color='b') we cn use long method for line dot graph
plt.annotate('Number of matches Team Batting First Won', xy=(2008, 22), xytext=(2008, 26),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
plt.annotate('Number of matches team Chasing Won', xy=(2008, 36), xytext=(2008, 40),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
plt.annotate('Number of times Match Tied', xy=(2008, 0), xytext=(2008, 4),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
'''sns.set(font_scale=1.6)
plt.figure(figsize=(13, 9))
cax = plt.imshow(tm_value, interpolation='nearest')'''
plt.title("IPL Data",fontsize=18,color='r')
#plt.colorbar()

plt.show()
plt.close()