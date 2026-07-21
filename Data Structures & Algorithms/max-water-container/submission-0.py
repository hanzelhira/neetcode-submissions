class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = 0
        k = len(heights) - 1
        large = 0

        while j < k:
            area = (k - j) * min(heights[k], heights[j])
            if heights[j] > heights[k]:
                large = max(large, area)
                k -= 1
            elif heights[j] < heights[k]:
                large = max(large, area)
                j += 1
            else:
                large = max(large, area)
                k -= 1
                j += 1
        return large

