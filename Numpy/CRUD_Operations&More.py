import numpy as np


# C R E A T E
''' empty()
arr = np.empty((3, 3))
print("empty array created with random values:")
print(arr)
# '''

''' zeros()
arr = np.zeros((3, 3))
print("array of zeros created:")
print(arr)
# '''

''' ones()
arr = np.ones((3, 3))
print("array of one created:")
print(arr)
# '''

''' full()
arr = np.full((3, 3, 3), 6)
print("array created:")
print(arr)
# '''

''' eye() identity matrix
arr = np.eye(3)
print("identity matrix:")
print(arr)
# '''

''' diag() diagonal matrix
arr = np.diag((1, 2, 3, 4, 5))  # given elements will be diagonal elements
print("diagonal matrix:")
print(arr)
# '''

''' arange()
arr = np.arange(1, 30, 5)  # here 1D array will be created from 1-30 & it will print every 5th element
print(f"array created: {arr}")
# '''

'''
# linspace()
arr = np.linspace(10, 50, 10)  # resultant array is going to have only 10 numbers from 1-50
# having same difference between each element
print(f"linspace arr: {arr}")

# reshape()  reshape an array without changing the total size.
print(arr.reshape(2, 5))

# resize()  resize an array changing the total size.
print(np.resize(arr, (3, 5)))

# pad()  enlarge and pad an array.
print(np.pad(arr, (3, 3)))

# repeat()  repeat elements of an array
print(arr.repeat(2))
# '''

''' random()
arr = np.random.randint(15, 25, size=(3, 3))
print("random values between given range:")
print(arr)
# '''

''' To disable this behaviour and force NumPy to print the entire array, 
# you can change the printing options using set_printoptions.
import sys
np.set_printoptions(threshold=sys.maxsize)
arr = np.arange(10000).reshape(100, 100)
print(arr)
# '''



# U P D A T E
# Indexing
''' arr1 is 1D array, so it has only one axis(0) which are cols
arr1 = np.array([1, 2, 3, 4, 5, 6])
print(f"the last element in arr1: {arr1[-1]}")
print(f"the first element in arr1: {arr1[0]}")
arr1[5] = 100
print(f"value updated is: {arr1}")
# '''

''' arr2 is 2D array, it has two axis(1 & 0) which is row & col
arr2 = np.array([
    [1, 2, 3, 4],
    [7, 8, 9, 10],
    [3, 6, 9, 8]
])
print(f"the last element in arr2: {arr2[0][-1]}")  # in 0th row last col
print(f"the first element in arr2: {arr2[0][0]}")  # in 0th row 0th col
arr2[1][2] = 96
print(f"value updated is: {arr2}")
# '''

''' 3D array
arr3 = np.array([
    [
        [1, 2, 3],
        [3, 2, 1]
    ],
    [
        [4, 5, 6],
        [6, 5, 4]
    ],
    [
        [7, 8, 9],
        [9, 8, 7]
    ]
])
""" 
arr3 is 3D array, so it will take 3 positional argument
I. see entire array as 1D array, which has three 2D array inside it arr3[0-2]
II. now in each 2D array there are two 1D array arr[0-1]
III. and each 1D array contains 3 elements arr3[0-2]
"""
print(f"arr3: {arr3[1][0][-1]}")
print(f"arr3: {arr3[1][0][2]}")
arr3[2][1][3] = 70
print(f"value updated is: {arr3}")
# '''


# Slicing
''' 1D array
a = np.arange(10)**3
print(a)
a[:6:2] = 1000  # from start to position 6, exclusive, set every 2nd element to 1000
print(a)
print(a[::-1])  # reverse
# '''


''' 2D array
def arry(x, y):
    return 10 * x + y


# arr = np.fromfunction(arry, (5, 4), dtype=int)
# print(arr)
# '''
# print(arr[1:])
# print(arr[1:2])
# NOTE:- `,` separates the row and column slicing
# print(arr[:])
# print(arr[:1])
# print(arr[1:])
# print(arr[1, :])
# print(arr[0, :1])
# print(arr[0, :])
# print(arr[1:2, -1])
# print(arr[2, 0:1])
# print(arr[3:, 3])
# print(arr[:, -1])
# print(arr[2:, -1])
# print(arr[2, 2:3])
# print(arr[-1:, -1])
# print(arr[1:, -1])
# print(arr[2:, :2])
# '''

''' 3D array
arr = np.array([
    [
        [1, 2, 3],
        [3, 2, 1]
    ],
    [
        [4, 5, 6],
        [6, 5, 4]
    ],
    [
        [7, 8, 9],
        [9, 8, 7]
    ]
])
# print(arr[:1, 1:])
# print(arr[0, 1:2])
# print(arr[:1])
# print(arr[1:])
# print(arr[-1:])
# print(arr[:2, :1])
# print(arr[:2, :1, :2])  # `:1` refers, here each 1D arr in 2D arr is considered as single col, so each 2D arr has 2 col
# print(arr[:2, :, :2])  # `:2` refers elements inside each col of 2D arr
# '''


# np.nditer() & flat
# iterating through all the elements in array
# for elements in arr.flat:
#     print(elements)
# for elements in np.nditer(arr[1]):  # we can also get specific rows & cols
#     print(elements)


# Index
# to know the exact position of element in array
# for row_col, element in np.ndenumerate(arr):
#     print(row_col, element)


''' append()
arr = np.array([
    [
        [1, 2, 3],
        [3, 2, 1]
    ],
    [
        [4, 5, 6],
        [6, 5, 4]
    ],
    [
        [7, 8, 9],
        [9, 8, 7]
    ]
])
a = np.arange(10)**3
new_arr = np.append(arr, a)
print(new_arr)  # it creates 1D array
# '''



# BASIC OPERATIONS

a = np.array([5, 10, 20, 3, 50])

b = np.array([[4, 5, 244, 47, 98],
              [33, 54, 74, 23, 19]])

c = np.array([[4, 5, 47],
              [54, 23, 19],
              [11, 71, 0]])

d = np.array([[5, 47, 98],
              [33, 23, 19],
              [-1, -80, -45]])
# print(f"a-b= {a-b}")
# print(f"a+b= {a+b}")
# print(f"a*b= {a*b}")  # element wise multiplication
# print(f"a/b= {a/b}")
# print(f"a//b= {a//b}")  # floor division
# print(f"a%b= {a%b}")
# print(f"a to the power b= {a**b}")
# print(f"sin of a= {np.sin(a)}")
# print(f"a AND b= {a&b}")
# print(f"a XOR b= {a^b}")
# print(f"a OR b= {a|b}")
# print(f"NOT b= {~b}")
# print(f"left shift b= {b<<2}")
# print(f"right shift a= {a>>2}")



# D E L E T E
# it takes index value of element as obj to delete element & it returns 1D array
# original array does not change
# print(np.delete(a, 1))
# print(np.delete(c, 1))
# print("row deleted:")
# print(np.delete(c, 2, axis=0))
# print("col deleted:")
# print(np.delete(c, 2, axis=1))
