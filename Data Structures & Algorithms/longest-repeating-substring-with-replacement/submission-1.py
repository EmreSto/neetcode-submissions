class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        current_longest = 0
        longest_len = 0
        my_dict = {}
        for R in range(len(s)):
            if s[R] not in my_dict:
                my_dict[s[R]] = 1
            else:
                my_dict[s[R]] += 1
            while (R - L + 1) - max(my_dict.values()) > k:
                my_dict[s[L]] -= 1
                L += 1
            current_longest = R - L + 1
            if current_longest > longest_len:
                longest_len = current_longest
        return longest_len

            

        