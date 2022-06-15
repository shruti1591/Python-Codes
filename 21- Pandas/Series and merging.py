# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:38:05 2021

@author: SYSTEMS
"""

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)


import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)


import pandas as pd
import numpy as np
data = {'a' : 0, 'b' : 1, 'c' : 2}
s = pd.Series(data)
print(s)


#Merging
import pandas as pd
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(left)
print(right)
print(pd.merge(left,right,on='id'))
print(pd.merge(left,right,on=['id','subject_id']))