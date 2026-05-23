class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, current, remaining):
            if remaining < 0:
                return
            if remaining == 0:
                res.append(current.copy())
                return
            if i >= len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                current.append(candidates[j])
                backtrack(j+1, current, remaining - candidates[j])
                current.pop()
        backtrack(0, [], target)
        return res




        