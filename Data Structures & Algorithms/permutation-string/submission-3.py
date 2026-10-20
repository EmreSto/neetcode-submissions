class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        my_dict = {}
        my_dict_s1 = {}
        L = 0
        for i in range(len(s1)):
            if s1[i] not in my_dict_s1:
                my_dict_s1[s1[i]] = 1
            else:
                my_dict_s1[s1[i]] += 1
        
        for R in range(len(s2)):
            if s2[R] not in my_dict:
                my_dict[s2[R]] = 1
            else:
                my_dict[s2[R]] +=1
            if R >= len(s1):
                my_dict[s2[R-len(s1)]] -= 1
                if my_dict[s2[R-len(s1)]] == 0:
                    del my_dict[s2[R-len(s1)]]
            if my_dict == my_dict_s1:
                return True
        return False
            
            
        






        