import pandas as pd
import numpy as np

df = pd.read_excel("./Timetable/new_mal_1.xlsx")
df=df.drop(columns='k')
df['SEC']=df['SEC'].astype(str)

#for i in range(0,len(df.index)):
#    df.iat[i,6]=str(df.iloc[i,6])


for i in range(0, len(df.index)):
    if df.iloc[i, 2] == "Tutorial" or df.iloc[i, 2] == "Practical":
        df.iat[i, 6] = "1"

j = 0
for i in range(0, len(df.index)):
    if df.iloc[i, 2] == "Tutorial":
        while True:
            df.iat[i+j, 6] = 'T'+str(df.iloc[i+j, 6])
            j += 1
            if i+j==len(df.index):
                j=0
                break
            if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                i = i+j-1
                j=0
                break
    elif df.iloc[i, 2] == "Practical":
        while True:
            df.iat[i+j, 6] = 'P'+str(df.iloc[i+j, 6])
            j += 1
            if i+j==len(df.index):
                j=0
                break
            if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                i = i+j-1
                j=0
                break
    elif pd.notnull(df['L'].iloc[i]) and df.iloc[i, 3] != 0:
        while True:
            df.iat[i+j, 6] = 'L'+str(df.iloc[i+j, 6])
            j += 1
            if i+j==len(df.index):
                j=0
                break
            if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                i = i+j-1
                j=0
                break
    elif pd.notnull(df['L'].iloc[i]) and df.iloc[i, 4] != 0 and df.iloc[i, 3] == 0:
        while True:
            df.iat[i + j, 6] = 'P' + str(df.iloc[i + j, 6])
            j += 1
            if i+j==len(df.index):
                j=0
                break
            if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                i = i+j-1
                j=0
                break

    elif pd.notnull(df['L'].iloc[i]) and df.iloc[i, 4] == 0 and df.iloc[i, 3] == 0 and pd.isnull(df['ROOM'].iloc[i]):
        while True:
            df.iat[i + j, 6] = 'PR0'
            j += 1
            if i+j==len(df.index):
                j=0
                break
            if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                i = i+j-1
                j=0
                break
    elif pd.notnull(df['L'].iloc[i]) and df.iloc[i, 4] == 0 and df.iloc[i, 3] == 0 and pd.notnull(df['ROOM'].iloc[i]):
        while True:
            df.iat[i + j, 6] = 'L' + str(df.iloc[i + j, 6])
            j += 1
            if i+j==len(df.index):
                j=0
                break
            if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                i = i+j-1
                j=0
                break

writer = pd.ExcelWriter("./Timetable/new_mal_2.xlsx")
df.to_excel(writer, 'Sheet1')
writer.save()



print(df.to_string())