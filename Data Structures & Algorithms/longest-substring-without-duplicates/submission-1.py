class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        #sliding window
        left = 0
        substring_length = 0
        for right in range(1, len(s)):
            # if character repeat, update longest substring
            while s[right] in s[left:right]:
                left+=1

            substring_length = max(substring_length, right - left + 1)
        return substring_length
            

