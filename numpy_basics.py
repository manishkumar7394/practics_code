#DIMENSION ARRAY , NDIM (NO. OF DIMENSION) def- data kitne direction/ axes me store hai

#zerro (0) dimension array [SCALAR]--def- sirf ek hi single value ho 
# a= np.array (10)
# print(a)                #output is 0 means 1 value 

# one (1) dimensoin array [VECTOR]-- def - jis array me value ek line me store ho aur isme output row me deta h
# import numpy as np
# arr_1d = np.array([10,20,30,40,50])
# print(arr_1d)             #output is that [10,20,30,40,50]


#2 diamantional array [MATRIX] -- def- array me row and columns dono ho 
# arr_2d = np.array([[1,2,3],
#                   [4,5,6]])
# print(arr_2d)


#   3- DIMENSION ARRAY [TENSOR] -- def- jab multiple 2-d array ek sath stocked ho jate h to 3-d array hota h aur ye layar me matrix banate hai
# import numpy as np
# a = np.array([
#               [[1,2,3],
#                [4,5,6]],

#               [[7,8,9],
#                [10,11,12]]
              
#              ])
# print(a.shape)                   shape = no of martrix , row, columns
# print(a)                        #show vlaue
# print(a.ndim)               #show the dimension like 3-d


# 🟢 Basic NumPy Practice Questions (Level 1)

# 1. Import NumPy
# Import NumPy in Python using the alias np.
# import numpy as np
# ⸻

# 2. Create a 1D Array
# one_d = np.array([10,20,30,40,50])
# print(one_d)

# Create a NumPy array with the following values:[10, 20, 30, 40, 50]
# arr= np.array([10, 20, 30, 40, 50])
# print(arr)

# 3. Check the Data Type - Print the type of the array.
# print(type(arr))            #np.ndarray

# 4. Check the Dimension- Print the number of dimensions of the array using ndim.
# arr= np.array([10, 20, 30, 40, 50])
# print(arr.ndim)                     output is 1

# 5. Check the Shape - Print the shape of the array.
#print(arr.shape)                output is (5,) means 5 elements

# 6. Find Total Elements - Print the size (total number of elements) in the array.
# print(arr.size)             output is 5

# 7. Indexing -Print the third element of the array.
# print(arr[2])                  output is 30

# 8. Slicing-  Extract the following elements from the array:[20, 30, 40]
# print(arr[1:4])                 #output is [20,30,40]

# 9. Create a 2D Array -Create the following 2D array:[[1,2,3],
                                                    # [4,5,6]]
# arr_2d = np.array([[1,2,3],
#                    [4,5,6]])
# print(arr_2d)


# 10. Check Rows and Columns
# For the above 2D array, print:
# 	•	the shape
# 	•	the number of dimensions
# arr= np.array([[[1,2,3],
#                 [4,5,6],
#                 [7,8,9]],                   #layar 1 martrix of 3
#                 [[1,2,3],
#                 [4,5,6],
#                 [7,8,9]],                   #layar 2 
#                 [[9,8,7],
#                 [6,5,4],
#                 [3,2,1]]                    #layar 3
#                 ])
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)


import numpy as np
# 🟡 Level 2 Questions
# 11. Create a Zeros Array
# arr= np.array(10)
# print(f"this is zerro dimensional array: {arr.ndim}")

# Create a 3×3 array filled with zeros.
# arr= np.zeros((3,3))
# print(arr)

# 12. Create a Ones Array - Create a 2×4 array filled with ones.
# arr_1= np.ones((2,4))
# arr_int= arr_1.astype(int)              #convert floating into int.
# print(arr_int)

# 13. Generate Random Numbers -Create a 3×3 array of random numbers.
# arr = np.random.randint(0,10,(3,3))
# print(arr)

# 14. Array Addition -Create two arrays:
# a = np.array ([10,2,20,30,40,50])
# b = np.array([12,23,34,4,55,66])
# print(a+b)

# 5. Array Multiplication- Multiply the same arrays element-wise.
# print(a*b)
# 16. Find the Sum -Find the total sum of this array:
# print(sum(a))
# print(sum(b))

# 7. Find the Mean Find the average (mean) of the array.
# total = sum(a)/len(a)
# print(total)                        #output is 25.3

# 18. Find the Maximum Value - Find the maximum value in the array.
# print(max(a))
# 19. Find the Minimum Value
# print(min(a))

# 20. Reshape an Array-  Convert the following array into a 2×3 matrix:[1,2,3,4,5,6]
# arr = np.array([1,2,3,4,5,6])
# reshape_arr = arr.reshape(2,3)
# print(reshape_arr)
