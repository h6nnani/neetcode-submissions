import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''.join(char for char in s.lower() if char.isalnum())
        return newstr == newstr[::-1]