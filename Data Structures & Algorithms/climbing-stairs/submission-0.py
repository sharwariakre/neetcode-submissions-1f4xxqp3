class Solution:
    def climbStairs(self, n: int) -> int:
        prevone, prevtwo = 1,1
        for i in range(n-1):
            temp = prevone
            prevone = prevone + prevtwo
            prevtwo = temp
        return prevone
        