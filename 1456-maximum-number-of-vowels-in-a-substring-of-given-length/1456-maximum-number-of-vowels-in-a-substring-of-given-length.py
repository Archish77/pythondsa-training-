class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cur_count = 0

        for i in range(k):
            if s[i] in vowels:
                cur_count += 1

        max_count = cur_count

        for i in range(k, len(s)):
            if s[i] in vowels:      
                cur_count += 1
            if s[i-k] in vowels:     
                cur_count -= 1

            max_count = max(max_count, cur_count)

        return max_count