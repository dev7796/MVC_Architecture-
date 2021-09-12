import pandas as pd
import numpy as np

number = int(input("Please enter the number for generating the number of datasets: "))

Type_Of_Disease_list =[np.NaN,'Autoimmune Diseases','Allergies & Asthma','Cancer','Celiac Disease','Crohns & Colitis','Heart Disease','Infectious Diseases','Liver Disease']
blood_Group_list = [np.NaN,'A+','A-','B+','B-','AB+','AB-','O+','O-']
Months_list = [np.NaN,'January','February','March','April','May','June','July','August','September','October','November','December']
year_list = [np.NaN,2013,2014,2015,2016,2017,2018,2019,2020]
Places_list = [np.NaN,'Rajkot','Vadodra','Surat','Gandhinagar','Ahmedabad','Anand','Bhuj','Jamnagar']
Person_Count_list=[np.NaN,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Blood_Quantity_list=[np.NaN,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Accident_List=[np.NaN,'Hereditary','Auto-Immune','Infectious','Natural-Cause','Contamination']
#alternative
#day_list = pd.DatetimeIndex(['2015-01-02','2016-05-05','2015-08-09'])

df= pd.DataFrame({"Type Of Disease" : np.random.choice(Type_Of_Disease_list, size=number),
                  "Blood Group" : np.random.choice(blood_Group_list, size = number),
                  "Month" : np.random.choice(Months_list, size = number),
                  "Year" : np.random.choice(year_list, size = number),
                  "Places" : np.random.choice(Places_list, size = number),
                  "Person Count" : np.random.choice(Person_Count_list, size = number),
                  "Blood Quantity" : np.random.choice(Blood_Quantity_list, size = number),
                  "Cause Of Disease" : np.random.choice(Accident_List, size=number)
                  })

print (df)
df.to_excel("BloodGroup.xlsx")