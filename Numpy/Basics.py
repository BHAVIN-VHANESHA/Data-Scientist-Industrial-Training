# Numerical Python(numpy) is the package in python used for mathematical operations

# importing package
import numpy as np
import time

# print(np.__version__)

# a = np.random.rand(1000000000)
''' List
start = time.time()
mean_list = sum(a)/len(a)
print(mean_list)
print(f"list time: {time.time() - start}")
# '''

''' Numpy
start = time.time()
mean_numpy = np.mean(a)
print(mean_numpy)
print(time.time() - start)
# '''


# Creating ndarray
''' 0D Array
arr = np.array(10)
print(f"array: {arr}")

# how to check array type
print(f"array type: {type(arr)}")

# how to check which dimension of array really is
print(f"dimension: {arr.ndim}")

# how to change dimension of array
arr = np.array(10, ndmin=1)
print(f"dimension changed to 1D: {arr}")

# how to check number of rows & cols
print(f"shape(row,col): {arr.shape}")

# how to check data type
print(f"data type: {arr.dtype}")
# the number in the end of datatype indicates space given to elements in bits(4 bytes)

# how to check total elements in an array
print(f"total elements: {arr.size}")
# return total number of elements in each col
print(f"total elements in each col: {np.size(arr, axis=0)}")
# return total number of elements in each row
# the below given print statement will give IndexError because this is 0D array,
# so single element is considered as col
# print(f"total elements in each row: {np.size(arr, axis=1)}")

# how to check storage capacity given to each element
print(f"stored each element in {arr.itemsize} bytes")
# how to check total storage given to elements in array
print(f"total storage of elements is {arr.nbytes} bytes")

# NOTE:- by default ndarray gives 8 bytes to each element
# '''

''' 1D Array
arr = np.array([1, 2, 3, 4, 5])
print(f"array: {arr}")
print(f"array type: {type(arr)}")
print(f"dimension: {arr.ndim}")
arr = np.array([1, 2, 3, 4, 5], ndmin=2)
print("dimension changed to 2D:")
print(arr)
print(f"shape(row,col): {arr.shape}")
print(f"data type: {arr.dtype}")
print(f"total elements: {arr.size}")
print(f"total elements in each col: {np.size(arr, axis=0)}")  # col(y-axis)
print(f"total elements in each row: {np.size(arr, axis=1)}")  # row(x-axis)
print(f"stored each element in {arr.itemsize} bytes")
print(f"total storage of elements is {arr.nbytes} bytes")
# '''

''' 2D Array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("array:")
print(arr)
print(f"array type: {type(arr)}")
print(f"dimension: {arr.ndim}")
print(f"shape(row,col): {arr.shape}")
print(f"total elements: {arr.size}")
print(f"total elements in each col: {np.size(arr, axis=0)}")  # col(y-axis)
print(f"total elements in each row: {np.size(arr, axis=1)}")  # row(x-axis)
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], ndmin=3)
print("dimension changed to 3D:")
print(arr)
print(f"data type: {arr.dtype}")
print(f"stored each element in {arr.itemsize} bytes")
print(f"total storage of elements is {arr.nbytes} bytes")
# '''

# ''' 3D Array
arr = np.array([
    [[1, 2, 3],
     [4, 5, 6]],
    [[7, 8, 9],
     [10, 11, 12]]
])
print("array:")
print(arr)
print(f"array type: {type(arr)}")
print(f"dimension: {arr.ndim}")
print(f"element at index 0: {arr[0][0][0]} at 0th position")
print(f"element at index 0: {arr[1][0][0]} at 1st position")
print(f"shape(1D size,2D size,3D size): {arr.shape}")
print(f"total elements in each col: {np.size(arr, axis=0)}")  # col(y-axis)
print(f"total elements in each row: {np.size(arr, axis=1)}")  # row(x-axis)
arr = np.array([
    [[1, 2, 3],
     [4, 5, 6]],
    [[7, 8, 9],
     [10, 11, 12]]
], ndmin=4, dtype=complex)
print("dimension changed to 4D:")
print(arr)
print(f"data type: {arr.dtype}")
print(f"total elements: {arr.size}")
print(f"stored each element in {arr.itemsize} bytes")
print(f"total storage of elements is {arr.nbytes} bytes")
# '''
