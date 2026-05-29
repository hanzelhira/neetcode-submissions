class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)

        need = res.most_common(k)

        result = []

        for val, count in need:
            result.append(val)
        
        return result