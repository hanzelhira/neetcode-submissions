class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        streak = 0

        for num in set_num:
            if (num - 1) not in set_num:
                current_num = num
                cur_streak = 1

                while (current_num + 1) in set_num:
                    cur_streak += 1
                    current_num += 1
                streak = max(streak, cur_streak)
        
        return streak

            

             


