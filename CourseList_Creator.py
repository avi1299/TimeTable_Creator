import pandas as pd
import numpy as np
import sys

# This code does the job of creating a DataFram of relevant data of all the courses to create a sort of course list
# Among the columns is a column LTPC
def CourseList_Creator(df,cc_list,writer):
    j=0
    index_list=[]
    for i in range(0, len(df.index)):
       if(df.iloc[i,0]==cc_list[j]):
           index_list+=[i]
           j+=1
           if j==len(cc_list):
               break
    j=0
    for i in index_list:
        while pd.isnull(df['COURSE TITLE'].iloc[i+j+1]) or df.iloc[i+j+1, 2] == "Tutorial" or df.iloc[i+j+1, 2] == "Practical":
            j+=1
        df1=df.iloc[i:i+j+1,:]
        df1=df1.reset_index(drop=True)
        j=0
        name1 = str(df.iloc[i,0])
        df1.to_excel(writer, sheet_name=name1)
      #  writer.save()
    writer.close()
    
    return df

if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("This script Requires a Two Arguments: the locations of the Source and Destination Excel Files in that order")
        exit(1)
    df = pd.read_excel(str(sys.argv[1]))
    #The new table has an extra column with the row numbers.  This was created while writing the dataframe into the Excel file.
    #We are removing it for furter processing. Remove the line below if you dont have such a column.
    #df = pd.read_excel("./Timetable/new_mal_4.xlsx")
    df=df.drop(df.columns[0], axis=1)
    
    #TODO: Create a way to input the courses 
    cc_list =[1003,1004,1006,1007,1010,1014,1015]
    #writer = pd.ExcelWriter("./Timetable/new_mal_5.xlsx") # pylint: disable=abstract-class-instantiated
    df=CourseList_Creator(df,cc_list,writer)
    #Writing the changes   
    writer = pd.ExcelWriter(str(sys.argv[2])) # pylint: disable=abstract-class-instantiated
   # print("Writing changes to :" + str(sys.argv[2]+"\nDone.."))
              