class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for char in s:
            if char not in dict_s:
                dict_s[char] = 1
            else:
                dict_s[char] +=1
        for c in t:
            if c not in dict_t:
                dict_t[c] =1
            else:
                dict_t[c] +=1
        if dict_s == dict_t:
            return True
        else:
            return False