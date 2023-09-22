import numpy as np


a = np.array([5, 10, 20, 3, 50])

b = np.array([[4, 5, 244, 47, 98],
              [33, 54, 74, 23, 19]])

c = np.array([[4, 5, 47],
              [54, 23, 19],
              [11, 71, 0]])

d = np.array([
            [5, 47, 98],
            [33, 23, 19],
            [-1, -80, -45]], dtype=float)

# print(f"a@b= {d@c}")  # matrix multiplication same as function matmul() (no. of rows and cols must be equal) & both
# array must be of same dimension
# print(f"d.c= {d.dot(c)}")  # dot product(no. of rows and cols must be equal) & both
# array must be of same dimension
# print(f"d.c= {np.dot(d, c)}")  # dot product(no. of rows and cols must be equal) &
# both array must be of same dimension


# Determinant
# np.linalg.det()  # linalg is linear algebra under which maths operations fall
# print(f"determinant of c: {np.linalg.det(c)}")

# Inverse
# np.linalg.inv()
# print(np.linalg.inv(c))

# Transpose (row elements become col elements and vise-versa)
# print(c.T)

# reciprocal()  [1/element]
# print(np.reciprocal(d))


# --------------- xxxxx ---------------

#  S T A T I S T I C S

# max()
# print(np.max(c))
# print(f"col: {np.max(c, axis=0)}")  # return max element from each col
# print(f"row: {np.max(c, axis=1)}")  # return max element from each row

# min()
# print(np.min(c))
# print(f"col: {np.min(c, axis=0)}")  # return min element from each col
# print(f"row: {np.min(c, axis=1)}")  # return min element from each row


# sum()
# print(np.sum(b))  # do the sum of all the elements in array
# print(f"col add: {np.sum(b, axis=0)}")  # do the sum of all the elements of col
# print(f"row add: {np.sum(b, axis=1)}")  # do the sum of all the elements of row

# cumsum()  cumulative sum
# print(np.cumsum(b))  # do the sum of all the elements in array
# print(f"col cumulative sum: {np.cumsum(b, axis=0)}")  # do the cumulative sum of all the elements of col
# print(f"row cumulative sum: {np.cumsum(b, axis=1)}")  # do the cumulative sum of all the elements of row


# argmax()
# print(np.argmax(b))  # return the index of greatest element
# print(np.argmax(b, axis=0))  # return the index of greatest element from each col
# print(np.argmax(b, axis=1))  # return the index of greatest element from each row

# argmin()
# print(np.argmin(b))  # return the index of greatest element
# print(np.argmin(b, axis=0))  # return the index of smallest element from each col
# print(np.argmin(b, axis=1))  # return the index of smallest element from each row


# around()
arr = np.array([0.5, 0.4, 0.9, 0.7, 0.1, 0.6, -1.0, -89.5, -100.9, -4.4])
# print(f"rounded value: {np.round(arr)}")
# print(f"rounded value: {np.round(arr, decimals=1)}")  # digits after `.`


# floor & ceil
# print(f"lower value: {np.floor(arr)}")
# print(f"upper value: {np.ceil(arr)}")


# mean()
# print(np.mean(a))
# print(np.mean(arr4))
# print(np.mean(arr1))


# sqrt()
# print(np.sqrt(a))
# print(np.sqrt(arr4))
# print(np.sqrt(arr2))
# print(np.sqrt(arr1))
# print(np.sqrt(arr3))


# square()
# print(np.square(a))
# print(np.square(b))
# print(np.square(arr4))
# print(np.square(arr1))


# --------------- xxxxx ---------------

#  COPY  &  VIEW
# NOTE:- copy() makes a temp change in array which does not reflect in original array but
# view() make change in original array
'''
arr_copy = a.copy()
print(f"copy array: {arr_copy}")
arr_copy[0] = 6
print(f"updated copy array: {arr_copy}")
print(f"original array: {a}")

arr_view = a.view()
print(f"view array: {arr_view}")
arr_view[0] = 4
print(f"updated view array: {arr_view}")
print(f"original array: {a}")
# '''
