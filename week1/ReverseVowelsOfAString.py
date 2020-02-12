class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 0:
            return s
        
        lst = list(s)
        leftVowelPos = 0
        rightVowelPos = len(lst) - 1
        vowels = 'aeiouAEIOU'
        
        while leftVowelPos < rightVowelPos:
            leftV = lst[leftVowelPos]
            rightV = lst[rightVowelPos]
            
            if leftV in vowels:
                if rightV in vowels:
                    lst[leftVowelPos], lst[rightVowelPos] = lst[rightVowelPos], lst[leftVowelPos]
                    leftVowelPos += 1
                    rightVowelPos -= 1
                    continue
                    
                else:
                    rightVowelPos -= 1
                    continue
                    
            else:
                leftVowelPos += 1
                
        return ''.join(lst)