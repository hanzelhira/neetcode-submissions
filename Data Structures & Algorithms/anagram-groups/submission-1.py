class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:

            ana = "".join(sorted(s))

            if ana not in groups:
                groups[ana] = []

            groups[ana].append(s)
        return list(groups.values())