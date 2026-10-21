class Solution:   
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        dict_s = {}
        result = []
        reslen = float("inf")
        L = 0
        for i in range(len(t)):
            if t[i] not in dict_t:
                dict_t[t[i]] = 1
            else:
                dict_t[t[i]] += 1
        have, need = 0, len(dict_t)
        for R in range(len(s)):
            if s[R] not in dict_s:
                dict_s[s[R]] = 1
            else:
                dict_s[s[R]] += 1
            if s[R] in dict_t and dict_s[s[R]] == dict_t[s[R]]:
                have +=1
            
            while have == need:
                if (R-L+1) < reslen:
                    result = [L, R]
                    reslen = (R-L+1)
                dict_s[s[L]] -= 1
                if s[L] in dict_t and dict_s[s[L]] < dict_t[s[L]]:
                    have -= 1
                L += 1
        if reslen == float("inf"):
            return ""
        left,right = result
        return s[left:right+1]
        



            


             
    
            
            