class Solution:
    def maxOperations(self, nums, k):
        count = {}
        ops = 0

        for num in nums:
            need = k - num
            if count.get(need, 0) > 0:
                ops += 1
                count[need] -= 1
            else:
                count[num] = count.get(num, 0) + 1

        return ops
