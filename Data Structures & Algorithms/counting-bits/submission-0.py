class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        counter = 0
        for i in range(n +1):
            output.append(bin(i).count('1'))
        return output
        