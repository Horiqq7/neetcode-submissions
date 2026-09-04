class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for number in num_set:
            sec = 1
            if number - 1 not in num_set:
                while (number + sec) in num_set:
                    sec += 1
            if ( sec > longest):
                longest = sec 
        return longest