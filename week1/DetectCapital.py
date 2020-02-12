class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        
        tail = word[1:]
        if word[0].islower():
            return tail.islower()
                
        else:
            return tail.islower() or tail.isupper()