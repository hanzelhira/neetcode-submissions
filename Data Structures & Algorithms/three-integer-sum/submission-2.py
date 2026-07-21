class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                if (sorted_nums[j] + sorted_nums[k] == -(sorted_nums[i])):
                        result.append([sorted_nums[j], sorted_nums[k], (sorted_nums[i])])
                        j += 1
                        k -= 1
                        while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                            j += 1
                elif (sorted_nums[j] + sorted_nums[k] > -(sorted_nums[i])):
                    k -= 1
                else:
                    j += 1
            
        return result


