class Solution:
    def isHappy(self, n: int) -> bool:
        check_set = set()
        while n != 1:
            if n in check_set:
                return False
            check_set.add(n)
            n = sum (d ** 2 for d in [int(d) for d in str(n)])
        return True




