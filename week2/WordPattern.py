class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        list_str = str.split(" ")
        
        pattern_to_str = {}
        seen_in_str = set()
        
        if len(pattern) != len(list_str):
            return False
        
        for i in range(len(pattern)):
            c = pattern[i]
            word = list_str[i]
            
            if c not in pattern_to_str:
                if word in seen_in_str:
                    return False
                pattern_to_str[c] = word
                seen_in_str.add(word)
                
            elif pattern_to_str[c] != word:
                return False
            
        return True