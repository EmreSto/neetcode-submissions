class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        L = 0
        current_len = 0
        longest_len = 0
        for R in range(len(s)):
            while s[R] in my_set:
                my_set.remove(s[L])
                L = L + 1
            current_len = R - L + 1
            my_set.add(s[R])
            if current_len > longest_len:
                longest_len = current_len
        return longest_len


            
        