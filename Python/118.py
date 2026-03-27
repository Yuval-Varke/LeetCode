# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


#  [https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif]

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]    #Initialize the res list with [1]
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]    #Padded the temp list with 0 
            row = []                      #Initialize the row list to append it in res list
            for j in range(len(res[-1])+1):  #Iterate through the temp list and append the sum of temp[j] and temp[j+1] 
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res