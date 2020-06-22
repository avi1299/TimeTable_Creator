import pandas as pd
import numpy as np
import sys

# This code does the job of creating a DataFram of relevant data of all the courses to create a sort of course list
# Among the columns is a column LTPC
def CourseList_Creator(df):
    
    
    return df
def main():
    if len(sys.argv)==3:
        print("This script Requires a Two Arguments: the locations of the Source and Destination Excel Files in that order")
        exit(1)
    df = pd.read_excel(str(sys.argv[1]))
    #The new table has an extra column with the row numbers.  This was created while writing the dataframe into the Excel file.
    #We are removing it for furter processing. Remove the line below if you dont have such a column.
    df = pd.read_excel("./Timetable/new_mal_3.xlsx")
    df=df.drop(df.columns[0], axis=1)
    df=CourseList_Creator(df)
    #Writing the changes   
    writer = pd.ExcelWriter("./Timetable/new_mal_4.xlsx")
    #writer = pd.ExcelWriter(str(sys.argv[2]))
    df.to_excel(writer, 'Sheet1')
    writer.save()
   # print("Writing changes to :" + str(sys.argv[2]+"\nDone.."))
              
main()