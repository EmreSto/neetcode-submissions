class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mystring = set()
        left = 0
        max_length =0

        for right in range(len(s)):
            while s[right] in mystring:
                mystring.remove(s[left])
                left = left +1
            mystring.add(s[right])
            if len(mystring) > max_length:
                max_length = len(mystring)
        return max_length

        