class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False
        
        s1_counts = Counter(s1)

        for i in range(len2-len1 +1):
            if Counter(s2[i:i+len1]) == s1_counts:
                return True
        return False

        