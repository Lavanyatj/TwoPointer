# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str):
        import string
        s = s.translate(str.maketrans('', '', string.punctuation + ' \t\n\r')).lower()
        i = 0
        j = len(s) - 1
        while i < len(s) // 2:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

s = Solution()
print(s.isPalindrome("mad,am"))