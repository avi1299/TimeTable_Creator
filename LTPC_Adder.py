import pandas as pd
import numpy as np
import sys

def LTPC_Adder(df):
    df['LTPC']=np.zeros(len(df.index))
    df['LTPC']=df['LTPC'].astype(object)
    ltpc=np.zeros(4)
    acro={
        'L':0,
        'T':1,
        'P':2,
        'C':3
    }
    j=0
    for i in range(0,len(df.index)):
        ltpc=np.zeros(4)
        df['LTPC'].iat[i]=ltpc
        if (pd.notnull(df['COM CD'].iloc[i])):
            j=0
            ltpc=np.zeros(4)
            while(1):
                if(df['SEC'].iloc[i+j]=='L1'):
                    ltpc[acro['L']]+=1
                elif(df['SEC'].iloc[i+j]=='T1'):
                    ltpc[acro['T']]+=1
                elif(df['SEC'].iloc[i+j]=='P1'):
                    ltpc[acro['P']]+=1
                elif(df['SEC'].iloc[i+j]=='L2'):
                    ltpc[acro['L']]+=2                    
                elif(df['SEC'].iloc[i+j]=='T2'):
                    ltpc[acro['T']]+=2                
                elif(df['SEC'].iloc[i+j]=='P1'):
                    ltpc[acro['P']]+=2
                if(pd.notnull(df['CH D'].iloc[i+j])):
                    if ltpc[acro['C']]==0:
                        ltpc[acro['C']]+=1
                    elif ltpc[acro['C']]==1:
                        ltpc[acro['C']]+=2
                j+=1
                if(i+j==len(df.index) or not pd.isnull(df['COM CD'].iloc[i+j])):
                    return
            df['LTPC'].iat[i]=ltpc
            i+=j
    return df
        


def main():
    if len(sys.argv)==3:
        print("This script Requires a Two Arguments: the locations of the Source and Destination Excel Files in that order")
        exit(1)
  #  df = pd.read_excel(str(sys.argv[1]))
    #The new table has an extra column with the row numbers.  This was created while writing the dataframe into the Excel file.
    #We are removing it for furter processing. Remove the line below if you dont have such a column.
    df = pd.read_excel("./Timetable/new_mal_3.xlsx")
    df=df.drop(df.columns[0], axis=1)
    df=LTPC_Adder(df)
    #Writing the changes   
    writer = pd.ExcelWriter("./Timetable/new_mal_4.xlsx")
    #writer = pd.ExcelWriter(str(sys.argv[2]))
    df.to_excel(writer, 'Sheet1')
    writer.save()
  #  print("Writing changes to :" + str(sys.argv[2]+"\nDone.."))
              
main()    