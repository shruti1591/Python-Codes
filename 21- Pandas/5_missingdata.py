# Fifth program ( Missing data )
import pandas as pd
#import xlrd
df=pd.read_csv("empdata1.csv")
print(df) # display missing data as NaN ( Not a number )
df1=df.fillna(0)
print(df1) # fill all missing data by 0
df1=df.fillna({"ename":"NAME MISSING","sal":0.0,"DOJ":"00-00-00"})
print(df1)
df1=df.dropna()# data cleaning i.e remove row having missing data
print(df1)
    
