class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pairs = len(nums)/2
        c = Counter(nums)
        p = 0
        for val in c.values():
            p += (val//2)
        return p == pairs
        