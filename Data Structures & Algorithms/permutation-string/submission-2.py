class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_counts = Counter(s1)
        
        window_counts = Counter(s2[:len1])

        if s1_counts == window_counts:
            return True

        for i in range(len1, len2):
            new_char = s2[i]
            window_counts[new_char] += 1
            

            old_char = s2[i - len1]
            window_counts[old_char] -= 1
            
            if window_counts[old_char] == 0:
                del window_counts[old_char]
                
            if window_counts == s1_counts:
                return True

        return False