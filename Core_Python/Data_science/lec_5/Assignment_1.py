import pandas as pd
import numpy as np

number = int(input("Please enter the number for generating the number of datasets: "))

Work_ex_list =[np.NaN,0,0,0,0,1,2,3,4]
Gre_list = [np.NaN,312,316,220,340,313,311,300,301,302,303,304,305,296,297,298,299,339,338,334,335,330,331,332,333,336]
Ielts_list = [np.NaN,6,6.5,7,7.5,8,8.5,9,9.5]
Gpa_list = [np.NaN,6.0,7.0,8.0,7,1,7.5,7.2,6.5,6.8,8.9,9.8,9.9,9.2,7,9,6.9,9.2,9.4,9.5,7.3,5.5,5.9,6.3]
Passing_year_list = [np.NaN,2013,2014,2015,2016,2017,2018,2019,2020]
Internships_list = [np.NaN,0,1,2,3,4]
Research_paper_list = [np.NaN,0,1,2,3,4]
Conference_attended_list = [np.NaN,0,1,2,3]
toefl_list=[np.NaN,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120]
University_list = [np.NaN,'Brown University','Princeton University','Yale University']
#alternative
#day_list = pd.DatetimeIndex(['2015-01-02','2016-05-05','2015-08-09'])

df= pd.DataFrame({"Work_Experience" : np.random.choice(Work_ex_list, size=number),
                  "GRE" : np.random.choice(Gre_list, size = number),
                  "IELTS" : np.random.choice(Ielts_list, size = number),
                  "TOEFL" : np.random.choice(toefl_list, size = number),
                  "GPA" : np.random.choice(Gpa_list, size = number),
                  "Passing Year" : np.random.choice(Passing_year_list, size = number),
                  "Internships" : np.random.choice(Internships_list, size = number),
                  "Research Paper" : np.random.choice(Research_paper_list, size= number),
                  "Confernce Attended" : np.random.choice(Conference_attended_list, size = number),
                  #"University allocated" : np.random.choice(University_list, size = number)
                  }).set_index("Work_Experience")
df["University"] = ''

index=0
for x in range(number):
    if (df.iloc[index,0] >= 330 and df.iloc[index,3] >= 8.0 and (df.iloc[index,1] >= 7.5 or df.iloc[index,2] > 110)):
        df.iloc[index,8] = "Columbia Univerisity"
        index += 1
    elif(df.iloc[index, 0] >= 320 and df.iloc[index, 3] >= 7.5 and (df.iloc[index, 1] >= 7.0 or df.iloc[index, 2] > 105)):
        df.iloc[index, 8] = "Cornell Univerisity"
        index += 1
    elif(df.iloc[index, 0] >= 310 and df.iloc[index, 3] >= 7.5 and (df.iloc[index, 1] >= 7.0 or df.iloc[index, 2] > 105)):
        df.iloc[index, 8] = "Harvard Univerisity"
        index += 1
    elif (df.iloc[index, 0] >= 305 and df.iloc[index, 3] >= 7.0 and (df.iloc[index, 1] >= 6.5 or df.iloc[index, 2] > 100)):
        df.iloc[index, 8] = "Dartmouth Univeristy"
        index += 1
    elif (df.iloc[index, 0] >= 300 and df.iloc[index, 3] >= 6.5 and (df.iloc[index, 1] >= 6.5 or df.iloc[index, 2] > 100)):
        df.iloc[index, 8] = "University of Pennsylvania"
        index += 1
    else:
        df.iloc[index,8] = np.random.choice(University_list)
        index += 1

#df["University allocated"] = ["Cornell Univerisity" if x in range(330,340) else np.random.choice(University_list) for x in df['GRE']]

print (df)
df.to_excel("University.xlsx")