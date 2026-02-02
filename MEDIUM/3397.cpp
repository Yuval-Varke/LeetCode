// 3397. Maximum Number of Distinct Elements After Operations
// You are given an integer array nums and an integer k.

// You are allowed to perform the following operation on each element of the array at most once:

// Add an integer in the range [-k, k] to the element.
// Return the maximum possible number of distinct elements in nums after performing the operations.

 

// Example 1:

// Input: nums = [1,2,2,3,3,4], k = 2

// Output: 6

// Explanation:

// nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

// Example 2:

// Input: nums = [4,4,4,4], k = 1

// Output: 3

// Explanation:

// By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].


class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int ans = 0, prev = -1e9;

        for (int i = 0; i < nums.size(); i++) {
            int l = max(nums[i] - k, prev + 1);
            if (l <= nums[i] + k) {
                prev = l, ans++;
            }
        }
        return ans;
    }
};