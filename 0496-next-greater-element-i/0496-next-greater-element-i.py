class Solution:
    def nextGreaterElement(self, nums1, nums2):

        result = []

        for num in nums1:

            found = False
            index = nums2.index(num)

            for j in range(index + 1, len(nums2)):
                if nums2[j] > num:
                    result.append(nums2[j])
                    found = True
                    break

            if not found:
                result.append(-1)

        return result