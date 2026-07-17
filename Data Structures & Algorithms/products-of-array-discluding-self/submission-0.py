class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        index = 1

        for i in range(n):

            res[i] = index

            index *= nums[i]

        index = 1

        for i in range(n - 1, -1, -1):

            res[i] *= index

            index *= nums[i]
        
        return res

            
        