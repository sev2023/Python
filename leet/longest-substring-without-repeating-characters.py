# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# !!!!!!!!!!!!!! Output Limit Exceeded !!!!!!!!!!!!!!!!!!

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                print(s[i:j])
                if len(s[i:j]) != len(set(s[i:j])): break
                if len(s[i:j]) > res:
                    res = len(s[i:j])
                
        # print([s[i:j] for i in range(len(s)) for j in range(i, len(s))])
        return  res
      
# 100 times of:
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ 
