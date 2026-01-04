// 1390. Four Divisors

// Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. 
// If there is no such integer in the array, return 0.

 

// Example 1:
// Input: nums = [21,4,7]
// Output: 32
// Explanation: 
// 21 has 4 divisors: 1, 3, 7, 21
// 4 has 3 divisors: 1, 2, 4
// 7 has 2 divisors: 1, 7
// The answer is the sum of divisors of 21 only.

// Example 2:
// Input: nums = [21,21]
// Output: 64

// Example 3:
// Input: nums = [1,2,3,4,5]
// Output: 0

class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        for(int i =0;i<n;i++){
            int k = nums[i];
            int res = 0;
            int cnt = 0;
            for(int d = 1;d<=k;d++){
                if(k % d == 0){
                    cnt++;
                    res +=d;
                }
                if(cnt>4){
                    break;
                }
            }
            if(cnt == 4){
                sum +=res;
            }
        }
        return sum;
    }
};