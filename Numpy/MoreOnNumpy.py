import numpy as np


arr1 = np.array([[10, 20, 30],
                 [40, 50, 60]])

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

# Stacking
'''
# 1. vstack()  joins the array vertically (row after row)
# NOTE:- while performing the vstack() no.of columns must be same of the arrays
print("vertical stack:")
a = np.vstack((arr1, arr2))
print(a)
print(a.shape)
# '''

'''
# 2. hstack()  joins the array horizontally (col after col)
# NOTE:- while performing the vstack() no.of rows must be same of the arrays
print("horizontal stack")
a = np.hstack((arr1, arr2))
print(a)
print(a.shape)
# '''

'''
# 3. dstack()  basically it converts an array into single col (all the elements are joined downwards)
# if 2 array then one column of 1st arr & second column of 2nd arr
# NOTE:- while performing the dstack() no.of rows & columns must be same of the arrays
arr3 = np.array([11, 56, 89, 35, 44])
# a = np.dstack((arr3, arr2))
# print(a)  # ValueError: all the input array dimensions must match exactly
a = np.dstack((arr1, arr2))
print("dstack:")
print(a)
print(a.shape)
# '''


# Spliting
# print(np.array_split(arr1, 3))
'''
# 1. hsplit()  splits column wise & return two diff array
print(np.hsplit(arr2, 3))

# 2. vsplit()  splits row wise & return two diff array
print(np.vsplit(arr2, 2))
# '''


''' Searching   returns the index values
print(np.where(arr2 == 5))
print(np.where(arr2 > 5))
print(np.where(arr2 < 5))
# '''


''' Sorting   array is sorted row wise
arr = np.array([[90, 20, 30],
                [110, 50, 60],
                [10, 2, 30],
                [40, 51, 6]
                ])
print(f"ascending order: {np.sort(arr)}")
print(f"descending order: {-np.sort(-arr)}")  # descending order

# it will return the index values of sorted elements
print(np.argsort(arr))
# '''


# ''' any() & all()
# for any() at least 1 condition must satisfy & for all() all the conditions must satisfy
# any()
# print(np.any(arr1 % 2 == 0))
# print(np.any(arr2 % 2 == 0))
# print("\n")
# all()
# print(np.all(arr1 % 2 == 0))
# print(np.all(arr2 % 2 == 0))
# '''


# ''' lcm()
n1 = 6
n2 = 68
n3 = 31
# print(np.lcm(n1, n2))
arr3 = np.array([[15, 21, 30],
                 [43, 5, 66]])

arr4 = np.array([[11, 2, 3],
                 [4, 51, 60]])
# print(np.lcm(arr3, arr4))

# reduce() helps to pass more than 2 parameters in lcm()
# print(np.lcm.reduce((n1, n2, n3)))
# print(np.lcm.reduce((arr1, arr3, arr4, arr2)))
# '''

# gcd()
# print(np.gcd(n3, n1))
# print(np.gcd.reduce((arr2, arr3, arr4)))


#  Linear Equation
a = np.array([[3, 10], [2, 7]])
b = np.array([12, 17])
# print(np.linalg.solve(a, b))


# Quadratic Equation
coeff = np.array([1, 4, 4])
# print(np.roots(coeff))


# vdot()  vector product((arr3[0][0] * arr4[0][0]) + ..... + (arr3[1][2] * arr4[1][2])))
# print(np.vdot(arr3, arr4))


# Weighted Mean   it will perform vdot() & divide it by weights
# average()
# print(np.average(arr1, weights=arr2))
