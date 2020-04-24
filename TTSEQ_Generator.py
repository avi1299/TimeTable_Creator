import pandas as pd
import numpy as np
import sys
#This code does the job of taking the Day and Hour (including Common Hour) of a particular section
#and entering 1's in their respective locations on a 6X11 matrix, representing a weeky timetable.
#The locations of 1's represents the timetable slots that would be filled on selection of that particular section.
# Eg.
# DAYS:	['T', 'Th', 'S']
# HOURS:	['2']
# TTSEQ:	[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  		[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  		[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  		[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  		[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  		[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

def TTSEQ_Generator(df):
    df['TTSEQ']=np.nan
    df['TTSEQ']=df['TTSEQ'].astype(object) # To be able to set A 2D array as a dataFrame element
    seq = np.zeros((6,11))
    for i in range(0,len(df.index)):
        df['TTSEQ'].iat[i]=seq
    weekday={'M':0,
            'T':1,
            'W':2,
            'Th':3,
            'F':4,
            'S':5,
            'nan':6
            }
    for i in range(0,len(df.index)):
        seq = np.zeros((6,11))
        if(not pd.isna(df['CH D'].iloc[i]) and not pd.isna(df['CH H'].iloc[i]!=np.nan)):
            days=str(df['CH D'].iloc[i]).split()
            hours=str(df['CH H'].iloc[i]).split()
            for day in days:
                for hour in hours:
                    seq[weekday[day],int(hour)-1]=1
            #print(days)
            #print(hours)
        if(not pd.isna(df['DAYS'].iloc[i]) and not pd.isna(df['HOURS'].iloc[i]!=np.nan)):
            days=str(df['DAYS'].iloc[i]).split()
            hours=str(df['HOURS'].iloc[i]).split()
            for day in days:
                for hour in hours:
                    seq[weekday[day],int(hour)-1]=1    
            #print(days)
            #print(hours)
            #print(seq)
        df['TTSEQ'].iat[i]=seq
    return df

def main():
    if len(sys.argv)!=3:
        print("This script Requires a Two Arguments: the locations of the Source and Destination Excel Files in that order")
        exit(1)
    df = pd.read_excel(str(sys.argv[1]))
    #The new table has an extra column with the row numbers.  This was created while writing the dataframe into the Excel file.
    #We are removing it for furter processing. Remove the line below if you dont have such a column.
    df=df.drop(df.columns[0], axis=1)
    df=TTSEQ_Generator(df)
    #Writing the changes    
    writer = pd.ExcelWriter(str(sys.argv[2]))
    df.to_excel(writer, 'Sheet1')
    writer.save()
    print("Writing changes to :" + str(sys.argv[2]+"\nDone.."))
    
main()

