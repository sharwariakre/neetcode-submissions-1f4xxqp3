class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, current, remaining):
            if remaining == 0:
                res.append(current.copy())
                return
            if remaining < 0:
                return
            if i >= len(nums):
                return
            current.append(nums[i])
            backtrack(i, current, remaining - nums[i])
            current.pop()
            backtrack(i+1, current, remaining)
        backtrack(0,[],target)
        return res