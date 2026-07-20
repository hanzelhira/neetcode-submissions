class Solution:
    def isPalindrome(self, s: str) -> bool:
        cur = "".join(filter(str.isalnum, s)).lower()

        rev = cur[::-1]

        if cur == rev:
            return True
        
        return False