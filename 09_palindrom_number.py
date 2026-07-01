class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        sum = 0
        rem = 0
        original = x
        while x > 0 :
            
            rem = x % 10
            sum = sum * 10 + rem 
            x = x//10
        return sum == original
    
# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 