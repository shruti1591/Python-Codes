# Fourth program
import pandas as pd
#import xlrd
df=pd.read_csv("empdata.csv",
               parse_dates=["DOJ"]) # display DOJ in YYYY-MM-DD form
print(df)
df1=df.sort_values("DOJ")# Sort records as per DOJ in Ascending order(Sen to Jr)
print(df1) # in case of tie data will be sorted as per index value
df1=df.sort_values("DOJ",ascending=False)# Sort Jr to Sr
print(df1)
#df1=df.sort_values(by=["DOJ","sal"],ascending=[False,True])
#print(df1)# sort by DOJ in decending order but if DOJ is same then sal is sorted
          # in ascending order

