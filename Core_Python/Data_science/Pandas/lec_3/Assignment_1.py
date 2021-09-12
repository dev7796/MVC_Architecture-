#Q.1

import pandas as pd
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
print(MatchData)
df4=MatchData.to_csv('file2')



'''
d2008=data.get_group(2008)
d2009=data.get_group(2009)
d2010=data.get_group(2010)
d2011=data.get_group(2011)
d2012=data.get_group(2012)
d2013=data.get_group(2013)
d2014=data.get_group(2014)
d2015=data.get_group(2015)
MatchData=pd.DataFrame({'Year':df['Year'].unique(),
                    'Total No of matches':[d2008['Year'].count(),
                                           d2009['Year'].count(),
                                           d2010['Year'].count(),
                                           d2011['Year'].count(),
                                           d2012['Year'].count(),
                                           d2013['Year'].count(),
                                           d2014['Year'].count(),
                                           d2015['Year'].count()],
                    'Number of matches Team Batting First Won':[df[(df['Year']==2008) & (df['Winning_Team']=='FirstBatting')].count().max(),
                                                                d2009[d2009['Winning_Team']=='FirstBatting'].count().max(),
                                                                d2010[d2010['Winning_Team']=='FirstBatting'].count().max(),
                                                                d2011[d2011['Winning_Team']=='FirstBatting'].count().max(),
                                                                d2012[d2012['Winning_Team']=='FirstBatting'].count().max(),
                                                                d2013[d2013['Winning_Team']=='FirstBatting'].count().max(),
                                                                d2014[d2014['Winning_Team']=='FirstBatting'].count().max(),
                                                                d2015[d2015['Winning_Team']=='FirstBatting'].count().max()],
                    #'Number of matches team Chasing Won':[d2008[d2008['Winning_Team']=='Chasing'].count().max(),
                    #                                      d2009[d2009['Winning_Team']=='Chasing'].count().max(),
                    #                                      d2010[d2010['Winning_Team']=='Chasing'].count().max(),
                    #                                     d2011[d2011['Winning_Team']=='Chasing'].count().max(),
                    #                                      d2012[d2012['Winning_Team']=='Chasing'].count().max(),
                    #                                      d2013[d2013['Winning_Team']=='Chasing'].count().max(),
                    #                                      d2014[d2014['Winning_Team']=='Chasing'].count().max(),
                    #                                      d2015[d2015['Winning_Team']=='Chasing'].count().max()],
                    #'Number of times Match Tied':[d2008[d2008['Winning_Team']=='Match Tied'].count().max(),
                    #                              d2009[d2009['Winning_Team']=='Match Tied'].count().max(),
                    #                              d2010[d2010['Winning_Team']=='Match Tied'].count().max(),
                    #                              d2011[d2011['Winning_Team']=='Match Tied'].count().max(),
                    #                               d2012[d2012['Winning_Team']=='Match Tied'].count().max(),
                    #                               d2013[d2013['Winning_Team']=='Match Tied'].count().max(),
                    #                              d2014[d2014['Winning_Team']=='Match Tied'].count().max(),
                    #                              d2015[d2015['Winning_Team']=='Match Tied'].count().max()]



                     })

print(MatchData.set_index('Year'))'''










'''d2010['Year'].count(),d2011['Year'].count(),
                                             d2012['Year'].count(),d2013['Year'].count(),
                                             d2014['Year'].count(),d2015['Year'].count()'''
'''for i in d2008('Winning_Team'):
    if i == 'FirstBatting':
        i=i+1
    elif i == 'Chasing':
        j=j+1
    else:
        k=k+1
total_no_matches=i+j+k
print(i,j,k,total_no_matches)'''


