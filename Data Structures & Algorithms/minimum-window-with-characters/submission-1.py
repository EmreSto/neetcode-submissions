class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_dict = {}
        t_dict = {}
        result = []
        reslen = float("inf")
        L = 0
        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] +=1
        have, need = 0 , len(t_dict)
        for R in range(len(s)):
            if s[R] not in s_dict:
                s_dict[s[R]] = 1
            else:
                s_dict[s[R]] +=1
            if s[R] in t_dict and s_dict[s[R]] == t_dict[s[R]]:
                have += 1
            while have == need:
                if (R-L +1) < reslen:
                    reslen = R-L+1
                    result = [L,R]
                s_dict[s[L]] -= 1
                if s[L] in t_dict and s_dict[s[L]] < t_dict[s[L]]:
                    have -=1
                L += 1
        if reslen == float("inf"):
            return ""
        left,right = result
        return s[left:right+1]
                
                
        