class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {}
        dict_s2 = {}

        for i in range(len(s1)):
            if s1[i] not in dict_s1:
                dict_s1[s1[i]] = 1
            else:
                dict_s1[s1[i]] +=1
        for R in range(len(s2)):
            if s2[R] not in dict_s2:
                dict_s2[s2[R]] = 1
            else:
                dict_s2[s2[R]] += 1
            if R >= len(s1):
                dict_s2[s2[R-len(s1)]] -= 1
                if dict_s2[s2[R-len(s1)]] == 0:
                    del dict_s2[s2[R-len(s1)]]
            if dict_s1 == dict_s2:
                return True
        return False     
                
            
        