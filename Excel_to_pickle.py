import pandas as pd
import numpy as np
import sys
import Labeller
import LTPC_Adder
import Name_Attacher
import TTSEQ_Generator

if __name__ =="__main__":
    if len(sys.argv)!=2:
        print("This script Requires an Argument: the location of the Source Excel File")
        exit(1)
    df = pd.read_excel(str(sys.argv[1]))
    #df = pd.read_excel("./Timetable/FS19.xlsx")
    df= Name_Attacher.Name_Attacher(df)
    df=Labeller.Labeller(df)
    df=TTSEQ_Generator.TTSEQ_Generator(df)
    df=LTPC_Adder.LTPC_Adder(df)
    df.to_pickle(str(sys.argv[1]).partition(".xlsx")[0]+".pkl")
    #df.to_pickle("./Timetable/FS19.pkl")
    print("Writing changes to Pickle file.\nDone..")

    #Writing Changes to Excel file
    writer = pd.ExcelWriter("./Timetable/View.xlsx") # pylint: disable=abstract-class-instantiated
    df.to_excel(writer, 'Sheet1')
    writer.save()
    
