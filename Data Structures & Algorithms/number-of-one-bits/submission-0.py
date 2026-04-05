class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        bin_n = bin(n)
        for i in bin_n:
            if i == '1':
                counter += 1
        return counter 
