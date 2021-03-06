import pandas as pd
import numpy as np
import sys

#This code does the job of prepend the type of class Lecture 'L', Practical 'P' and Tutorial 'T'
#to the section number so that each row of the table has a combined code like L1, T6 or P4.
#Project Type courses(which do not have section number) have a a code 'PR0'
#Eg.
#
#1001	BIO F110	BIOLOGY LABORATORY	0	2	1	1	BHAGAVATULA VANI (904)	    3219	T	1 2	M	1	6163	30/11    FN
#						                            2	Neelam Mahala (RS) (628)	3219	M	3 4	M	1		
#						                            3	Meghana Tare (599)	        3219	M	6 7	M	1		
#						                            4	Sumukh Thakar (RS) (1,065)	3219	M	8 9	M	1		
#						                            5	Anirudh Sahu (RS) (786)	    3219	M	1 2	M	1		
#						                            6	Tripti Mishra (RS) (200)	3219	T	3 4	M	1		
#
# to
#
#1001	BIO F110	BIOLOGY LABORATORY	0	2	1	P1	BHAGAVATULA VANI (904)	    3219	T	1 2	M	1	6163	30/11    FN
#						                            P2	Neelam Mahala (RS) (628)	3219	M	3 4	M	1		
#						                            P3	Meghana Tare (599)	        3219	M	6 7	M	1		
#						                            P4	Sumukh Thakar (RS) (1,065)	3219	M	8 9	M	1		
#						                            P5	Anirudh Sahu (RS) (786)	    3219	M	1 2	M	1		
#						                            P6	Tripti Mishra (RS) (200)	3219	T	3 4	M	1		
			
def Labeller(df):
    df['SEC']=df['SEC'].astype(str)
    #Adding Section Numbers to the Subjects where there is a single Tutorial or Practical
    for i in range(0, len(df.index)):
        if df['COURSE TITLE'].iloc[i] == "Tutorial" or df['COURSE TITLE'].iloc[i] == "Practical":
            df['SEC'].iat[i] = "1"


    j = 0
    for i in range(0, len(df.index)):
        if df['COURSE TITLE'].iloc[i] == "Tutorial":
            while True:
                df['SEC'].iat[i+j] = 'T'+(df['SEC'].iloc[i+j])
                j += 1
                if i+j==len(df.index):
                    j=0
                    break
                if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                    i = i+j-1
                    j=0
                    break
                
        elif df['COURSE TITLE'].iloc[i] == "Practical":
            while True:
                df['SEC'].iat[i+j] = 'P'+(df['SEC'].iloc[i+j])
                j += 1
                if i+j==len(df.index):
                    j=0
                    break
                if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                    i = i+j-1
                    j=0
                    break
                
        elif pd.notnull(df['L'].iloc[i]) and df['L'].iloc[i] != 0:
            while True:
                df['SEC'].iat[i+j] = 'L'+(df['SEC'].iloc[i+j])
                j += 1
                if i+j==len(df.index):
                    j=0
                    break
                if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                    i = i+j-1
                    j=0
                    break
                
        elif pd.notnull(df['L'].iloc[i]) and df['P'].iloc[i] != 0 and df['L'].iloc[i] == 0:
            while True:
                df['SEC'].iat[i + j] = 'P' + (df['SEC'].iloc[i + j])
                j += 1
                if i+j==len(df.index):
                    j=0
                    break
                if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                    i = i+j-1
                    j=0
                    break

        elif pd.notnull(df['L'].iloc[i]) and df['P'].iloc[i] == 0 and df['L'].iloc[i] == 0 and pd.isnull(df['ROOM'].iloc[i]):
            while True:
                df['SEC'].iat[i + j] = 'PR0'
                j += 1
                if i+j==len(df.index):
                    j=0
                    break
                if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                    i = i+j-1
                    j=0
                    break
                
        elif pd.notnull(df['L'].iloc[i]) and df['P'].iloc[i] == 0 and df['L'].iloc[i] == 0 and pd.notnull(df['ROOM'].iloc[i]):
            while True:
                df['SEC'].iat[i + j] = 'L' + (df['SEC'].iloc[i + j])
                j += 1
                if i+j==len(df.index):
                    j=0
                    break
                if pd.notnull(df['COURSE TITLE'].iloc[i+j]):
                    i = i+j-1
                    j=0
                    break

    for i in range(0, len(df.index)):
        if ".0" in df['SEC'].iloc[i]:
            df['SEC'].iat[i]=df['SEC'].iloc[i].partition(".")[0]
    return df

if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("This script Requires a Two Arguments: the locations of the Source and Destination Excel Files in that order")
        exit(1)
    df = pd.read_excel(str(sys.argv[1]))
    #df = pd.read_excel("./Timetable/new_mal_1.xlsx")
    #The new table has an extra column with the row numbers.  This was created while writing the dataframe into the Excel file.
    #We are removing it for furter processing. Remove the line below if you dont have such a column.
    df=df.drop(df.columns[0], axis=1)
    df=Labeller(df)
    #Writing the changes    
    writer = pd.ExcelWriter(str(sys.argv[2])) # pylint: disable=abstract-class-instantiated
    #writer = pd.ExcelWriter("./Timetable/new_mal_2.xlsx")
    df.to_excel(writer, 'Sheet1')
    writer.save()
    print("Writing changes to :" + str(sys.argv[2]+"\nDone.."))

