import pandas as pd

def doubleDataFrame(df):
    dfNew = pd.concat([df,df],axis=0).reset_index().copy()

    return dfNew