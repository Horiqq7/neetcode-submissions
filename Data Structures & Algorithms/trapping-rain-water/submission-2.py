class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        prefixe = [0] * n
        sufixe = [0] * n
        
        prefixe[0] = height[0]
        for i in range(1, n):
            prefixe[i] = max(prefixe[i - 1], height[i])
            
        sufixe[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            sufixe[i] = max(sufixe[i + 1], height[i])
            
        total = 0
        for i in range(n):
            total += min(prefixe[i], sufixe[i]) - height[i]
            
        return total