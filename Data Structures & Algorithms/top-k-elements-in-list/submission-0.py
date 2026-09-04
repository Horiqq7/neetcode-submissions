class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for number in nums:
            freq[number] = freq.get(number, 0) + 1
        sorted_pairs = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        
        return [item[0] for item in sorted_pairs[:k]]