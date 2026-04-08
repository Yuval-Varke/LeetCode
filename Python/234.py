# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:
# [https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg]

# Input: head = [1,2,2,1]
# Output: true
# Example 2:
# [https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg]

# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # skip middle if odd
        if fast:
            slow = slow.next

        # reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # compare
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True