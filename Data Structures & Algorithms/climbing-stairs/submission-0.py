class Solution:
    def climbStairs(self, n: int) -> int:
        way1=1
        way2=2
        count = 0
        if n == 1:
            return way1
        if n== 2:
            return way2
        for i in range(3, n+1):
            temp = way1 + way2
            way1 = way2
            way2 = temp
        return way2



