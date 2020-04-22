import pandas as pd
import numpy as np

df = pd.read_excel("./Timetable/new_mal_2.xlsx")
df['TTSEQ']=np.nan
df['TTSEQ']=df['TTSEQ'].astype(object)
seq = np.zeros((6,11))
for i in range(0,len(df.index)):
    a=df.iloc[i,9]
    b=np.loadtxt(str(a))
    print(b)