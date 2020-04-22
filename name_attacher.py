import pandas as pd
df = pd.read_excel("./Timetable/new_mal.xlsx")
j=0
for i in range(0,len(df.index)):
    if pd.isnull(df['SEC'].iloc[i]) and pd.isnull(df['ROOM'].iloc[i]):
        while pd.isnull(df['SEC'].iloc[i+j]) and pd.isnull(df['ROOM'].iloc[i+j]):
            df.iat[i - 1, 7] = df.iloc[i - 1, 7] + ', ' + df.iloc[i+j, 7]
            j += 1
            if i+j==len(df.index):
                break
        i = i+j
        j = 0
df = df.dropna(subset=['SEC', 'ROOM'], how='all').reset_index(drop=True)

print(df.to_string())

writer = pd.ExcelWriter("./Timetable/new_mal_1.xlsx")
df.to_excel(writer, 'Sheet1')
writer.save()