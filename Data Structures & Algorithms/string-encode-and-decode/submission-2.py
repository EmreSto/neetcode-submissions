class Solution:

    def encode(self, strs: List[str]) -> str:
        my_list =[]
        for strin in strs:
            strin_len = len(strin)
            my_list.append(str(strin_len)+"#"+strin)
        main_string ="".join(my_list)
        return main_string
    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            j = index
            while s[j] != "#":
                j +=1
            string_len = int(s[index:j])
            real_string = s[j+1: j+1 + string_len]
            result.append(real_string)
            index = j+1+string_len
        return result

