class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        l = 0
        r = 0
        ans = []
        while r < n:
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            if (r - l + 1) == k:
                ans.append(nums[queue[0]])
                if queue[0] == l:
                    queue.popleft()
                l += 1
            r += 1
        return ans

