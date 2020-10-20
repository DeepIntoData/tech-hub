import pandas as pd 
from connections import readMongoCloud


def RE_cleaner():
    
    #use list from JSON NEIGHBORHOOD READER TO PARSE REAL ESTATE MASTER TO SORT
    
    db_df = readMongoCloud("Real_Estate","San_Fran")
    
    df1=db_df.sort_values('RegionName', ascending=True)

    return df1
