
#1. What does Pandas stand for?
It is a python package for fast and efficient pocessing of tabular data, time series, matrix data, ect. Python Data Analysis Library 
# 2. What are the 2 collections used in Pandas?
motpltlib, Scipy
# 3. Name 4 things Pandas can do for us.
Import Data set, merge, rebuild missing data, stardardize data


# 4. To permanently sort a DataFrame, which keyword should one use 
# with the `df.sort()` method?



# 5. What is a CSV?
Data file 

# 6. When cleaning data what values do we not like in our data?
Null


#7. Import NumPy, use one of the NumPy methods and create 
# an array with a shape of (2, 3, 2). 
# You can use the reshape method -- `.reshape()`

import numpy as np

a1 = np.array([2, 3, 2])
print("a1 ...\n", a1)



import numpy as np

aArray = np.array([[1,2,3], [4,5,6]])
bArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("aArray original shape ...\n", aArray)

newShape1 = np.reshape(aArray, 6) 
print("newShape1 ...", newShape1)

newShape2 = bArray.reshape(3, 2, 2) 
print("\n reshaping bArray ...\n", newShape2)



# 8. Use NumPy `.linspace()` to create an array with 
# 6 linearly spaced values between 0 and 20

import numpy as np
a = np.linspace(0, 20)
print("Array a ...", a)


# 9. Make a Deep Copy of the above array

import copy
a = [[0.          0.40816327  0.81632653  1.2244898   1.63265306  2.04081633
  2.44897959  2.85714286  3.26530612  3.67346939  4.08163265  4.48979592
  4.89795918  5.30612245  5.71428571  6.12244898  6.53061224  6.93877551
  7.34693878  7.75510204  8.16326531  8.57142857  8.97959184  9.3877551
  9.79591837 10.20408163 10.6122449  11.02040816 11.42857143 11.83673469
 12.24489796 12.65306122 13.06122449 13.46938776 13.87755102 14.28571429
 14.69387755 15.10204082 15.51020408 15.91836735 16.32653061 16.73469388
 17.14285714 17.55102041 17.95918367 18.36734694 18.7755102  19.18367347
 19.59183673 20.        ]


# 10. Concatenate these 3 arrays into a new array named 'newArray'...
#     ```python

# Import the module


# OR import and alias the module for easy inline use
import numpy as np

a1 = np.aArray([[25, 16]])
print('a1 ...\n', a1)
b1 = np.bArray([[11, 2], [13, 4]])
print('b1 ...\n', b1)
c1 = np.cArray([[7, 81], [5, 6], [11, 12]])
print('c1 ...\n', c1)

# 11. Sort 'newArray' in order into 'sortedArray'

# 12. Unpack the array tuples from the above 'reshapedArray'  
# into 4 well named variables. # Print the 4 variables.


# 13. Combined and sort the following arrays into one called 'comboArray' ...

#     ```python
#         one = ([10, 11, 12, 13, 14, 15, 16, 17])
#         two = ([20, 21, 22, 23, 24, 25, 26, 27])
#         three = ([ 0, 1, 2, 3, 4, 5, 6, 7])
#     ```


# 14. Take 'comboArray' and perform the following slicing activities:
#     - print sec1 - the 2nd element
#     - print sec2 - all elements from the 3rd element to the last
#     - print sec3 - all elements from the 4th to the 14th elements
#     - print sec4 - the last 6 elements
#     - print sec5 - all element from #0 up to and including #15, using the negative number method, i.e. taking a section from the end.
#     - print sec6 - from #20 every even element to the end
#     - print sec7 - from the last element moving forward, every 5th element.
#
# 
#  15. Using `Series`, create a `DataFrame` that looks like this:

#     | Ingredients | Quantity | Unit |
#     |----|----|----|
#     | Flour | 4 | cups |
#     | Milk | 1 | cup |
#     | Eggs | 2 | large |
#     | Spam | 1 | can |

#     Name: Dinner, dtype: object



# 16. Take this data and create a DataFrame named studentData
#     ```Python
#         {'Name': ['Jai', 'janusha', 'Gaurav', 'Anuj'],
#             'Height': [5.1, 6.2, 5.1, 5.2],
#             'Qualification': ['Msc', 'MA', 'Msc', 'Msc'],
#             'address': ['Delhi', 'Doha', 'Chennai', 'Dakhar'],
#             'Age': [21, 23, 24, 21],
#             'Pets': ['Dog', 'Bunny', 'Chinchilla', 'Parrot'],
#             'sport': ['Darts', 'Basketball', 'PaddleBoarding', 'Cricket']
#         }
#     ```


# 17. Add a new column to the DataFrame with the following deserts:
#         ["ice cream", "Cashew Fudge", "waffels", "Carrot Halwa"]


# 18. Sort the 'studentData' DataFrame in Ascending order -- Sorting by column 'Name' and then "address"


# 19. Save this `DataFrame` here below to disc as a `.CSV` file with the name `cows_and_goats.csv`:

#     ```python
#        df = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
#     ```

# 20. (A) Using Pandas, make your own .CSV file with data on vegetables and save it. (B) Using Pandas, make a change to your CSV file, and save a copy with a different name.


