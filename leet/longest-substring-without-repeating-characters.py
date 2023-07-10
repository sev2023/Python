# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# !!!!!!!!!!!!!! Output Limit Exceeded !!!!!!!!!!!!!!!!!!

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        i = 0
        while i < len(s) - res:
            
            rr = 0              
            for j in range(i+1, len(s)+1):
                if len(s[i:j]) != len(set(s[i:j])): break
                rr += 1
            if rr  > res:
                res = rr
            i += 1
            
        # print([s[i:j] for i in range(len(s)) for j in range(i, len(s))])
        return  res
      
# 100 times of:
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ 
