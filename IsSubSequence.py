#https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isSubsequence(self, s:str, t:str):
        i = 0
        for j in range(len(t)):
            if i <len(s) and s[i]==s[j]:
                i +=1
        return i == len(s)

subseq = Solution()
print(subseq.isSubsequence("abc", "ahbgdc"))
