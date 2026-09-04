import array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        f = []
        productA = 1
        productB = 1
        for number in nums:
            a.append(productA)
            productA = productA * number
            
        
        for number in reversed(nums):
            b.append(productB)
            productB = productB * number
        
        b.reverse()

        for i in range(len(nums)):
            f.append(a[i] * b[i])

        return f