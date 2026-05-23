class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current, visited):
            if len(current) == len(nums):
                res.append(current)
                return
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                cur_element = nums[i]
                backtrack(current + [cur_element], visited)
                visited.remove(cur_element)

        backtrack([], set())
        return res

