class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        mv=nums[0]

        for v in nums:
            sum+=v
            mv = max(mv,sum)

            if sum<0:
                sum=0
        return mv