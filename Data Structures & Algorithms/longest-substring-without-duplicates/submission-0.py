class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        presentChar = set()
        for right in range(len(s)):
            if s[right] not in presentChar:
                presentChar.add(s[right])
            else:
                while s[right] in presentChar:
                    presentChar.remove(s[left])
                    left += 1
                presentChar.add(s[right])

            ans = max(ans, len(presentChar))
        return ans

            
