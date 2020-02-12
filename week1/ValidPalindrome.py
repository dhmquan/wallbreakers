class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = [c for c in s if c.isalnum()]
        s = ''.join(lst)
        
        l = len(s)
        for i in range(l // 2):
            if s[i] != s[l - i - 1]:
                return False
            
        return True