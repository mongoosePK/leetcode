# ToLowerCase.py
# william pulkownik
# leetcode problem to try and make the fastest string case lowering function


class Solution:
    def toLowerCase(self, s: str) -> str:
        '''
        There a 2 solutions here. 

        # one line statement with O(n) time complexity (below)
        return "".join(chr(ord(c) + 32) if c >= 'A' and c <= 'Z' else c for c in s)
        '''
        #another, faster, solution
        res=""
        for val in str:
            if ord(val)>=65 and ord(val)<=90:
                res+=chr(ord(val)+32)
            else:
                res+=val
                
        return res