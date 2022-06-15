# -*- coding: utf-8 -*-
"""


@author: SYSTEMS
"""

#Create the prices dictionary:
prices={}
 #Add values
fruit1=input("enter")
i=int(input("enter"))
prices[fruit1]=i
prices["apple"]= 2
prices["orange"]= 1.5
prices["pear"]= 3
print(prices)
#Create the stock dictionary
stock={}
#Add values

stock["banana"]= 6
stock["apple"]= 0
stock["orange"] =32
stock["pear"]= 15
print(stock)
 #Show all prices and stock
for food in prices:
      print (food)
      print ("prices:", prices[food])
      print ("stock:", stock[food])

total=0
for price in prices:
     money= prices[price]*stock[price]
     print (money)
     total=total +money
 
print ("The total money is", total)



