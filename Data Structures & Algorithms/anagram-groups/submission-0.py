class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            mydict[key].append(word)
        return list(mydict.values())

            

        

        