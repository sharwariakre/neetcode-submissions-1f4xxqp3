class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        left = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in res:
                res.add(s[i])
            else:
                while s[i] in res:
                    res.remove(s[left])
                    left+=1
                res.add(s[i])
            ans = max(ans, len(res))
        return ans
