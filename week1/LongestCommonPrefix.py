class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        commonPrefix = []
        for i in range(len(strs[0])):
            prefix = strs[0][i]
            for j in range(1, len(strs)):
                word = strs[j]
                if (i >= len(word)) or (word[i] != prefix):
                    return ''.join(commonPrefix)
                
            commonPrefix.append(prefix)
            
        return ''.join(commonPrefix)