class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current, visited):
            if len(current) == len(nums):
                res.append(current.copy())
                return
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                backtrack(current + [nums[i]], visited)
                visited.remove(nums[i])
        backtrack([], set())
        return res