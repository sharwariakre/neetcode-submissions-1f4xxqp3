class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in res:
                res[sorted_str] = [str]
            else:
                res[sorted_str].append(str)
        return list(res.values())