class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
               newStr += c.lower()
        return True if newStr == newStr[::-1] else False