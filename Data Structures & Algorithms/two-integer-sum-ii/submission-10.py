class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = {}
        l = 0
        left = numbers[l]
        r = len(numbers) - 1
        right = numbers[r]
        
        while l < r:
            if (left + right) > target:
                r -= 1
                right = numbers[r]
            elif (left + right) < target:
                l += 1
                left = numbers[l]
            else:
                return [l + 1, r + 1]
