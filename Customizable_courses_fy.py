import pandas as pd
import numpy as np

df = pd.read_excel("./Timetable/test_3_v2.xlsx")

writer = pd.ExcelWriter("./Timetable/Cust_course_fy.xlsx")

j=0
cc_list =[1001,1002,1003,1005,1007,1008,1009,1011,1012,1013,1015]
index_list=[]
for i in range(0, len(df.index)):
       if(df.iloc[i,0]==cc_list[j]):
           index_list+=[i]
           j+=1
           if j==len(cc_list):
               break
j=0

for i in index_list:
    while pd.isnull(df['COURSE TITLE'].iloc[i+j+1]) or df.iloc[i+j+1, 2] == "Tutorial" or df.iloc[i+j+1, 2] == "Practical":
        j+=1
    df1=df.iloc[i:i+j+1,:]
    df1=df1.reset_index(drop=True)
    j=0
    name1 = str(df.iloc[i,0])
    df1.to_excel(writer, sheet_name=name1)
    writer.save()
    print(df1.to_string())
writer.close()

