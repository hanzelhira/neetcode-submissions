class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        seen = set()
        item = list(s)
        for i in range(len(item)):
            val = item[i]
            if val not in seen:
                seen.add(val)
                best = max(best, len(seen))
            elif val in seen:
                while val in seen:
                    seen.remove(item[left])
                    left += 1
                seen.add(val)
        
        return best





