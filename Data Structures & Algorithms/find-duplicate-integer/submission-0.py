class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return max(freq, key=freq.get)