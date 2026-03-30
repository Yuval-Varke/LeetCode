# 1189. Maximum Number of Balloons
# Solved
# 1182
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:
# [https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG]

# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2


# Example 3:
# [https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG]

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.




class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text = Counter(text)
        b_text = Counter("balloon")
        res = len(text)
        for ch in b_text:
            res = min(res,count_text[ch]//b_text[ch])
        return res