class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxsec = 0
        start = 0
        chars = {}

        for stop in range(len(s)):
            char = s[stop]

            if char in chars and chars[char] >= start:
                start = chars[char] + 1
            
            chars[char] = stop
            
            sec = stop - start + 1
            if sec > maxsec:
                maxsec = sec

        return maxsec