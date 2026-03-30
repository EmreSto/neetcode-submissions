class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = []
        for char in s:
            if char.isalnum() == True:
                char_lower = char.lower()
                clean_s.append(char_lower)
        new_str = ''.join(clean_s)
        if new_str == new_str[::-1]:
            return True
        else:
            return False