class Solution:

    def encode(self, strs: List[str]) -> str:
        my_list = []
        for strin in strs:
            strin_len = len(strin)
            my_list.append(str(strin_len)+"#"+strin)
        full_strin = "".join(my_list)
        return full_strin
    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            strin_length = int(s[index:j]) 
            strin = s[j + 1: j+1+strin_length]
            result.append(strin)
            index = j + 1 + strin_length
        return result








