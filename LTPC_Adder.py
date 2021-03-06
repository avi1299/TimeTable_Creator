import pandas as pd
import numpy as np
import sys

# This code does the job of creating a new column called 'LTPC' which is a numpy vector of length 4.
# Each element of the vector corresponds to Lecture 'L', Tutorial 'T', Practical 'P', and Common Hour 'C'.
# The numbers in these locatins indicate:
#     1:Single L/T/P/C class
#     2:Multiple classes but in the same time slot
#     3:Multiple classes with different time slots
# In case of 1, there is no choice of professor or timing.
# In case of 2, there is choice of professor only. Timing is fixed. (Most tutorial classes)
# In case of 3, there is choice of both professor and timing. (Lecture classes of large capacity courses)

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
        #df['LTPC'].iat[i]=ltpc
        if (pd.notnull(df['COM CD'].iloc[i])):
            j=0
            ltpc=np.zeros(4)
            while(1):
                if(df['SEC'].iloc[i+j]=='L1'):
                    ltpc[acro['L']]=1
                elif(df['SEC'].iloc[i+j]=='T1'):
                    ltpc[acro['T']]=1
                elif(df['SEC'].iloc[i+j]=='P1'):
                    ltpc[acro['P']]=1
                elif(df['SEC'].iloc[i+j]=='L2'):
                    ltpc[acro['L']]=2                    
                elif(df['SEC'].iloc[i+j]=='T2'):
                    ltpc[acro['T']]=2                
                elif(df['SEC'].iloc[i+j]=='P2'):
                    ltpc[acro['P']]=2
                if(pd.notnull(df['CH D'].iloc[i+j])):
                    if ltpc[acro['C']]==0:
                        ltpc[acro['C']]=1
                    elif ltpc[acro['C']]==1:
                        ltpc[acro['C']]=2
                j+=1
                if(i+j==len(df.index) or not pd.isnull(df['COM CD'].iloc[i+j])):
                    break
                df['LTPC'].iat[i+j]=np.nan
            df['LTPC'].iat[i]=ltpc
            i+=j
    i=0
    j=0
    for i in range(0,len(df.index)):
        if (pd.notnull(df['COM CD'].iloc[i])):
            base=i
            j=0
        if(df['LTPC'].iat[base][acro['L']]==2):
            if(df['SEC'].iloc[i+j]=='L2'):
                j=0
                while(df['SEC'].iloc[i+j]!='L1'and df['SEC'].iloc[i+j]!='P1' and df['SEC'].iloc[i+j]!='T1' and df['SEC'].iloc[i+j]!='PR0'):
                    if(str(df['TTSEQ'].iat[i+j])!=str(df['TTSEQ'].iat[i+j-1])):
                        df['LTPC'].iat[base][acro['L']]=3
                    j+=1
                    if(pd.notnull(df['COM CD'].iloc[i+j])):
                        i+=j-1
                        break
        if(df['LTPC'].iat[base][acro['T']]==2):               
            if(df['SEC'].iloc[i+j]=='T2'):
                j=0
                while(df['SEC'].iloc[i+j]!='L1'and df['SEC'].iloc[i+j]!='P1' and df['SEC'].iloc[i+j]!='T1' and df['SEC'].iloc[i+j]!='PR0'):
                    if(str(df['TTSEQ'].iat[i+j])!=str(df['TTSEQ'].iat[i+j-1])):
                        df['LTPC'].iat[base][acro['T']]=3
                    j+=1
                    if(pd.notnull(df['COM CD'].iloc[i+j])):
                        i+=j-1
                        break
        if(df['LTPC'].iat[base][acro['P']]==2):    
            if(df['SEC'].iloc[i+j]=='P2'):
                j=0
                while(df['SEC'].iloc[i+j]!='L1'and df['SEC'].iloc[i+j]!='P1' and df['SEC'].iloc[i+j]!='T1' and df['SEC'].iloc[i+j]!='PR0'):
                    if(str(df['TTSEQ'].iat[i+j])!=str(df['TTSEQ'].iat[i+j-1])):
                        df['LTPC'].iat[base][acro['P']]=3
                    j+=1
                    if(pd.notnull(df['COM CD'].iloc[i+j])):
                        i+=j-1
                        break
        if(i>=len(df.index)):
            break
        i+=1
    return df
        


if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("This script Requires a Two Arguments: the locations of the Source and Destination Excel Files in that order")
        exit(1)
    df = pd.read_excel(str(sys.argv[1]))
    #df = pd.read_excel("./Timetable/new_mal_3.xlsx")
    #The new table has an extra column with the row numbers.  This was created while writing the dataframe into the Excel file.
    #We are removing it for furter processing. Remove the line below if you dont have such a column.
    df=df.drop(df.columns[0], axis=1)
    df=LTPC_Adder(df)
    #Writing the changes   
    writer = pd.ExcelWriter(str(sys.argv[2])) # pylint: disable=abstract-class-instantiated
    #writer = pd.ExcelWriter("./Timetable/new_mal_4.xlsx")
    df.to_excel(writer, 'Sheet1')
    writer.save()
    print("Writing changes to :" + str(sys.argv[2]+"\nDone..")) 
  