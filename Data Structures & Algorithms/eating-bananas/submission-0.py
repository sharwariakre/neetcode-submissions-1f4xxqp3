class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        
        while low <= high:
            hours = 0
            mid = (low + high) // 2
            for i in piles:
                hours += (i + mid - 1) // mid
            if hours > h:
                low = mid + 1
            elif hours <= h:
                ans = mid
                high = mid - 1
        return ans