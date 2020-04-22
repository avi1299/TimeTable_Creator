import pandas as pd
import numpy as np

df = pd.read_excel("./Timetable/test_3_v2.xlsx")

writer = pd.ExcelWriter("./Timetable/Cust_course.xlsx")


index_list =[]
#print(df.to_string())

j = 0
for i in range(0, len(df.index)):
    if pd.notnull(df['COURSE TITLE'].iloc[i]) and df.iloc[i, 2] != "Tutorial" and df.iloc[i, 2] != "Practical":
        if i==len(df.index)-1:
            break
        if pd.isnull(df['COURSE TITLE'].iloc[i+1]):
            index_list += [i]
        elif (df.iloc[i+1,2]=="Practical" or df.iloc[i+1,2]=="Tutorial") and pd.isnull(df['COURSE TITLE'].iloc[i+2]):
            index_list+=[i]

        # if i==len(df.index)-1:
        #     index_list += [i]
        #     break
        # while pd.isnull(df['COURSE TITLE'].iloc[i+j+1]) or "Tutorial" == df.iloc[i + j + 1, 2] or df.iloc[i + j + 1, 2] == "Practical":
        #     if df.iloc[i+j+1, 6]=="L2" or df.iloc[i+j+1, 6]=="T2" or df.iloc[i+j+1, 6]=="P2":
        #         index_list += [i]
        #         j=0
        #         break
        #     j+=1
        #     if i+j==len(df.index):
        #         j=0
        #         break

#print(index_list)
j=0
for i in index_list:
    while pd.isnull(df['COURSE TITLE'].iloc[i+j+1]) or df.iloc[i+j+1, 2] == "Tutorial" or df.iloc[i+j+1, 2] == "Practical":
        j+=1
    df1=df.iloc[i:i+j+1,:]
    df1.reset_index()
    j=0
    name1 = str(df.iloc[i,0])
    df1.to_excel(writer, sheet_name=name1)
    writer.save()
    print(df1.to_string())
writer.close()

