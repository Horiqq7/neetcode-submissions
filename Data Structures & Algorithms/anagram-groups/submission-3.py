class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}
        for s in strs:
            cheie = "".join(sorted(s))
        
            if cheie not in sol:
                sol[cheie] = []
            
            sol[cheie].append(s)
        return list(sol.values())
