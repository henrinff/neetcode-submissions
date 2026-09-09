class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        reverse = s[::-1]
        if s == reverse:
            return True
        else:
            return False