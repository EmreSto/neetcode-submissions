class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = format(n, '032b')
        reversed_string = new_n[::-1]
        return int(reversed_string,2)