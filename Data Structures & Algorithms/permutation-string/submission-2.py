class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = {}
        s2_match_counter = {}
        for i in s1:
            s1_counter[i] = 1 + s1_counter.get(i, 0)
        l = 0
        r = len(s1)-1

        for i in range(len(s1)):
            s2_match_counter[s2[i]] = 1 + s2_match_counter.get(s2[i], 0)
        
        while r < len(s2):
            if s1_counter == s2_match_counter:
                return True
            s2_match_counter[s2[l]] -= 1
            if s2_match_counter[s2[l]] == 0:
                del s2_match_counter[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                s2_match_counter[s2[r]] = 1 + s2_match_counter.get(s2[r], 0)
        return False


