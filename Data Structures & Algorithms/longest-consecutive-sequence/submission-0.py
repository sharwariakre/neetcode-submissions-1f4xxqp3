class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_c = 0

        for i in nums_set:
            if i - 1 not in nums_set:
                c = 1
                while i + 1 in nums_set:
                    c += 1
                    i += 1
                max_c = max(max_c, c)
        return max_c