#transforms data from *.mat (matlab table) to *.csv (comma separated values table), with predefined header
import os
import pandas as pd
import numpy as np
import scipy.io

def f_dif(f1, timest):
    """Transforms data from *.mat (matlab table) to *.csv (comma separated values table)
    This script was develop to transform a dataset from the LANL experimental tests, regarding the “Bookshelf Frame Structure - DSS 2000”.
    f_1_List, timest_List:
      - List of raw data folder paths, corresponding to each scenario
      - List of initial timestamps for each scenario
    Returns a set of csv files:
      - Header is predefined
      - Channel name convetion follows ray data convention
      - 9th column data is corrupted and thus replaced by 26th column data
    """

    if os.path.exists(f1):        
        fnames1 = os.listdir(f1) 

        for i in fnames1:

            name = i[:-4]

            col_array = [['3B','3B','3A','3A','3C','3C','3D','3D','2B','2B','2A','2A','2C','2C','2D','2D','1B','1B','1A','1A','1C','1C','1D','1D','SHK'],
                        [21,23,21,23,21,23,21,23,21,23,21,23,21,23,21,23,21,23,21,23,21,23,21,23,14],
                        [1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600,1600],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name,name],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

            path1 = f1 + i  
            if os.path.exists(path1): 
                try:
                    # load matlab data file
                    mat = scipy.io.loadmat(path1)
                    # remove matlab header
                    mat = {k:v for k, v in mat.items() if k[0] != '_'}
                    # transform dict_values to np array prepared to dataframe
                    mat3 = np.array(list(mat.values()))[0,:,:]
                    # create dataframe
                    data = pd.DataFrame(mat3)
                    #print(data.head())
                    # replace col 9 (corrupted) by col 26 (good), and drop old 26
                    data[8] = data[25]
                    data.drop([25], axis=1, inplace=True)
                    # insert final header
                    data.columns = col_array
                    print(data.head())
                    # save as cvs, named by increasing timestamp
                    data.to_csv(str(timest) + ".csv", index=False)

                    timest += 1000

                except Exception as e:  
                    print("ERROR:", e)
    else:
        data = []

    return(data)

# Call function
# Define Folder Paths
f_1_List = ["C:/.../LANL/Book_2000_udam1/udam1/",
        "C:/.../LANL/Book_2000_udam2/udam2/",
        "C:/.../LANL/Book_2000_udam3/udam3/",
        "C:/.../LANL/Book_2000_udam4/udam4/",
        "C:/.../LANL/Book_2000_udam5/udam5/",
        "C:/.../LANL/Book_2000_Dam_L1C_A/Dam1/",
        "C:/.../LANL/Book_2000_Dam_L3A/Dam2/",
        "C:/.../LANL/Book_2000_Dam_L13/Dam3/",
        "C:/.../LANL/Book_2000_Dam_L1C_B/Dam4/"]
# Define daily timestamps
timest_List = [1641031200, #Saturday, 1 January 2022 10:00:00
            1641117600,
            1641204000,
            1641290400,
            1641376800,
            1641463200,
            1641549600,
            1641636000,
            1641722400]  #Saturday, 9 January 2022 10:00:00
            
if len(f_1_List) == len(timest_List):
    for z1 in range(len(f_1_List)):
        #print(z1)
        res = f_dif(f_1_List[z1], timest_List[z1])
