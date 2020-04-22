import pandas as pd
import numpy as np

df = pd.read_excel("./Timetable/new_mal_2.xlsx")
df['TTSEQ']=np.nan
df['TTSEQ']=df['TTSEQ'].astype(object)
seq = np.zeros((6,11))

for i in range(0,len(df.index)):
    for j in [9,10,11,16]:
        if df.iloc[i,j]=="M":
            df.iloc[i,j]=1
        elif df.iloc[i,j]=="T":
            df.iloc[i,j]=2
        elif df.iloc[i, j] == "W":
            df.iloc[i, j] = 3
        elif df.iloc[i,j]=="Th":
            df.iloc[i,j]=4
        elif df.iloc[i,j]=="F":
            df.iloc[i,j]=5
        elif df.iloc[i, j] == "S":
            df.iloc[i, j] = 6

for i in range(0,len(df.index)):
    for j in [9,10,11]:
        if pd.notnull(df.iloc[i,j]):
            for k in [12,13,14,15]:
                if pd.notnull(df.iloc[i,k]):
                    seq[int(df.iloc[i, j])-1, int(df.iloc[i, k])-1] += 1
    if pd.notnull(df.iloc[i,16]):
        seq[int(df.iloc[i, 16]) - 1, int(df.iloc[i, 17]) - 1] += 1
    df.iat[i,20]=seq

    seq = np.zeros((6, 11))

for i in range(0,len(df.index)):
    for j in [9,10,11,16]:
        if df.iloc[i,j]==1:
            df.iat[i,j]="M"
        elif df.iloc[i,j]==2:
            df.iat[i,j]="T"
        elif df.iloc[i, j] == 3:
            df.iat[i, j] = "W"
        elif df.iloc[i,j]==4:
            df.iat[i,j]="Th"
        elif df.iloc[i,j]==5:
            df.iat[i,j]="F"
        elif df.iloc[i, j] == 6:
            df.iat[i, j] = "S"
print(df.to_string())



writer = pd.ExcelWriter("./Timetable/new_mal_3.xlsx")
df.to_excel(writer, 'Sheet1')
writer.save()

