# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1) > len(nums2):
            seen = Counter(nums1)
            for i in range(len(nums2)):
                if nums2[i] not in ans and nums2[i] in seen:
                    ans.append(nums2[i])
        elif len(nums1) <= len(nums2):
            seen = Counter(nums2)
            for i in range(len(nums1)):
                if nums1[i] not in ans and nums1[i] in seen:
                    ans.append(nums1[i])
        return ans