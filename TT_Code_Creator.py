import pandas as pd
import numpy as np

TT=np.zeros(6,11)

def T_T_Create(COM_COD):
    df = pd.read_excel("./Timetable/Cust_course_fy.xlsx", sheet_name=COM_COD)
#    print(df.to_string())

    x = df.iloc(0,6)
    while(df.iloc(i,6)[0]==x[0]):


