class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l, r = 0, 0
        ans = []
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if (r - l + 1) == k:
                ans.append(nums[q[0]])
                if q[0] == l:
                    q.popleft()
                l += 1
            r += 1
        return ans
