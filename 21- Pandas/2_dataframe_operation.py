# Second program
import pandas as pd
#import xlrd
df=pd.read_csv("empdata.csv" )
print(df)
print("Max salary: ",df["sal"].max())
print("Min salary:", df["sal"].min())
print(df.describe()) # display important information
print(df[df.sal >5000])# display records having sal more than 5000
print(df[df.sal ==df.sal.max()])# display record having max salary
print(df[["empid","ename"]][df.sal >5000])# display id&name which satisfy criteria
