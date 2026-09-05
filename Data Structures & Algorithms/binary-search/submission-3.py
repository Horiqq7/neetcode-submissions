class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        d = len(nums) - 1
        while (s <= d):
            m = (s + d) // 2
            if (nums[m] < target):
                s = m + 1
            elif (nums[m] > target):
                d = m - 1
            else:
                return m
        return -1