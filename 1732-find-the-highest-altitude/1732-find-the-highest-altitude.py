class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        max_alt = 0      

        for i in range(len(gain)):
            current += gain[i]                
            max_alt = max(max_alt, current)   

        return max_alt