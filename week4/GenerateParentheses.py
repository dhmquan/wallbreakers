class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        table = [['']]
        
        for j in range(1, n + 1):
            out = []
            
            for i in range(j):
                for x in table[i]:
                    for y in table[j - i - 1]:
                        out.append('(' + x + ')' + y)
                        
            table.append(out)
            
        return table[n]
        