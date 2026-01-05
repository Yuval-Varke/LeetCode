// 1975. Maximum Matrix Sum
`https://leetcode.com/problems/maximum-matrix-sum/description/`

// You are given an n x n integer matrix. You can do the following operation any number of times:

// Choose any two adjacent elements of matrix and multiply each of them by -1.
// Two elements are considered adjacent if and only if they share a border.

// Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.


// Example 1:


// Input: matrix = [[1,-1],[-1,1]]
// Output: 4
// Explanation: We can follow the following steps to reach sum equals 4:
// - Multiply the 2 elements in the first row by -1.
// - Multiply the 2 elements in the first column by -1.

// Example 2:


// Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
// Output: 16
// Explanation: We can follow the following step to reach sum equals 16:
// - Multiply the 2 last elements in the second row by -1.



// Approach :- If even number of negatives present in the matrix, 
//             then they can be cut each other off through the operation; Just return the sum.

// If odd number of neagtives in matrix, then only one will be left at the end after operations;
// return the differnce of sum and twice of the smallest element.


class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int small_val = INT_MAX;
        long sum = 0;
        int cnt = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                sum += abs(matrix[i][j]);
                if(matrix[i][j] < 0){
                    cnt++;
                }
                small_val = min(small_val,abs(matrix[i][j]));
            }
        }
        if(cnt%2==0){
            return sum;
        }
        return sum - (2*small_val);
    }
};