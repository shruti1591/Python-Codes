# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:46:14 2021

@author: SYSTEMS
"""


#SciPy is an open-source Python library which is used to solve 
#scientific and mathematical problems. It is built on the NumPy 
#extension and allows the user to manipulate and visualize 
#data with a wide range of high-level commands. 



'''Linear Algebra:
Linear algebra deals with linear equations and their representations 
using vector spaces and matrices. SciPy is built on  ATLAS LAPACK 
and BLAS libraries and is extremely fast in solving problems related
 to linear algebra. In addition to all the functions from numpy.linalg,
 scipy.linalg also provides a number of other advanced functions. 
 Also, if numpy.linalg is not used along with ATLAS LAPACK and 
 BLAS support, scipy.linalg is faster than numpy.linalg. '''


#Finding the Inverse of a Matrix:
import numpy as np
from scipy import linalg
A = np.array([[1,2], [4,3]])
B = linalg.inv(A)
print(B)



#Finding the Determinants:
import numpy as np
from scipy import linalg
A = np.array([[1,2], [4,3]])
B = linalg.det(A)
print(B)