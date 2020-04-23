import pandas as pd
import sys
#This code does the job of taking the names of instructors that teach the same section 
#which is present on more than one row of the ecxcel sheet and merge them in a comma seperated
#form so that each row of the excel sheet has an assocaiated section
#Eg.
#
#1002	BIO F111	GENERAL BIOLOGY	3	0	3	1	RAJDEEP CHOWDHURY (229)	                        5105	M W F	9				11/12    AN
#							                        Manoj Kannan (393)							
#						                        2	Manoj Kannan (393)	                            5105	T Th S	4				
#							                        Rajdeep Chowdhury (229)	
#
# to
#
#1002	BIO F111	GENERAL BIOLOGY	3	0	3	1	RAJDEEP CHOWDHURY (229), Manoj Kannan (393)	    5105	M W F	9				11/12    AN
#						                        2	Manoj Kannan (393), Rajdeep Chowdhury (229)	    5105	T Th S	4				


def Name_Attacher(src,dest):
    df = pd.read_excel(str(src))
    j=0
    #Checking the rows where the clumn of SEC and ROOM are empty
    for i in range(0,len(df.index)):
        if pd.isnull(df['SEC'].iloc[i]) and pd.isnull(df['ROOM'].iloc[i]):
            while pd.isnull(df['SEC'].iloc[i+j]) and pd.isnull(df['ROOM'].iloc[i+j]):
                df.iat[i - 1, 7] = df.iloc[i - 1, 7] + ', ' + df.iloc[i+j, 7]
                j += 1
                if i+j==len(df.index):
                    break
            i = i+j
            j = 0
    #Deleting the extra lines
    df = df.dropna(subset=['SEC', 'ROOM'], how='all').reset_index(drop=True)
    #print(df.to_string())
    writer = pd.ExcelWriter(str(dest))
    df.to_excel(writer, 'Sheet1')
    writer.save()
    return

def main():
    if len(sys.argv)!=3:
        print("This script Requires a Two Arguments: the locations of the Source and Destination Excel Files in that order")
        exit(1)
    Name_Attacher(str(argv[1],argv[2]))
    return