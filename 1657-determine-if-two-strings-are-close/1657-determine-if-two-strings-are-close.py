class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = {}
        count2 = {}

        for ch in word1:
            if ch in count1:
                count1[ch] += 1
            else:
                count1[ch] = 1

        for ch in word2:
            if ch in count2:
                count2[ch] += 1
            else:
                count2[ch] = 1

        # condition 1: same characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # condition 2: same frequencies
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True