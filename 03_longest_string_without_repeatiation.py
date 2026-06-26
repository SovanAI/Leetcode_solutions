class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        hash_set = set()
        for right in range(len(s)):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
        

        # longest substring without repeating characters
        # Given a string s, find the length of the longest substring without duplicate characters.