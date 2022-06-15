# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:58:40 2020

@author: SYSTEMS
"""

import re

Nameage="""Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21"""

ages=re.findall(r'\d{1,3}', Nameage)
names=re.findall(r'[A-Z][a-z]*',Nameage)
ageDict={}
x=0
for eachname in names:
    ageDict[eachname]=ages[x]
    x+=1
print(ageDict)
    

import re
if re.search("inform","We need to inform him with the latest information"):
    print("There is inform")
    

import re
allinform=re.findall("inform","We need to inform him with the latest information")
for i in allinform:
    print(i)

import re
str="we need to inform him with the latest information"
for i in re.finditer("inform",str):
    loctup=i.span()
    print(loctup)
    
import re
str="Sat, hat, mat, pat"
allstr=re.findall("[shmp]at",str)
for i in allstr:
    print(i)
    
import re
str="Sat, hat, mat, pat"
allstr=re.findall("[h-m]at",str)
for i in allstr:
    print(i)   
    
import re
str="Sat, hat, mat, pat"
allstr=re.findall("[^h-m]at",str)
for i in allstr:
    print(i)


import re
food="hat rat mat pat"
regex=re.compile("[r]at")
food=regex.sub("food",food)
print(food)

import re
randstr="here is \\drogba"
print(re.search(r"\\drogba",randstr))

import re
randstr="""Keep the blue flag 
flying high """
print(randstr)
regex=re.compile("\n")
randstr=regex.sub(" ",randstr)
print(randstr)

#\b: backspace
#\f: formfeed
#\r: carriage return
#\t: tab
#\v: vertical tab

import re
randstr="12345"
print("Matches:", len(re.findall("\d",randstr)))

import re
num="123 1234 12344 123456 1234567"
print("Matches:",len(re.findall("\d{5,7}",num)))


import re

#\w {a-zA-Z0-9}
#\w {^a-zA-Z0-9}

phn="194-888-2343"
if re.search("\d{3}-\d{3}-\d{4}",phn):
    print("it is a phone number")
    

import re
#\s [\f\n\r\t\v]
#\s [^\f\n\r\t\v]

if re.search("\w{2,20}\s\w{2,20}","Shruti Agrawal"):
    print("fullname is valid")
    

import re
email="sk@aol.com nm @.com @ab.com"
print("Email matches:",len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email)))

#Using Regular expressions to files
import re
f=open("mails.txt","r")
for line in f:
    res=re.findall(r'\S+@\S+',line)
    
if len(res)>0:
    print(res)
f.close()


import re
str='one two there one two three'
result=re.findall(r't[\w]*\Z',str)
print(result)