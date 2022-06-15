# first program
import pandas as pd
#import xlrd
df=pd.read_excel("empdata.xlsx")
print(df)
print("Dataframe Dimension: ", df.shape) # display rows and column in dataframe
r,c=df.shape
print("Rows in dataframe: ", r)
print("Column in dataframe: ", c)
print("First 5 rows:\n",df.head()) # by default
print("last 5 rows:\n",df.tail())# display last 2 column
print("Range of rows:\n",df[2:5])# range of rows
print(df[0::2]) # display alternate rows
print(df[5:0:-1])# reverse order
print(df.columns)# get column names
print(df.empid)# get column data
print(df.ename)# get column data
print(df[["empid","ename"]]) # getting multiple column data



import pandas as pd
empdata=[(101,102000),(102,100000)]
df=pd.DataFrame(empdata,columns=["eno","sal"])
print(df)