class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        postfix = []
        left_max = 0
        right_max = 0
        total = 0

        for i in range(len(height)):
            val = height[i]
            left_max = max(left_max, val)
            prefix.append(left_max)
        
        for i in range(len(height) - 1, -1, -1):
            val = height[i]
            right_max = max(right_max, val)
            postfix.insert(0, right_max)

        for i in range(len(height)):
            total += min(prefix[i], postfix[i]) - height[i]
        
        return total



        
            
            



        