class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        for i in range(len(s)):

            # Odd length palindrome
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1

            # Even length palindrome
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1

        return s[start:start + max_len]

        # the leetcode solution is correct and implements the expand around center approach to find the longest palindromic substring in a given string. It checks for both odd and even length palindromes by expanding from each character in the string. The time complexity of this solution is O(n^2), where n is the length of the input string, and the space complexity is O(1) since it uses a constant amount of extra space.