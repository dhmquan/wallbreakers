class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        out = []
        for row in A:
            newRow = row[-1::-1]
            newRow = map(lambda x: x ^ 1, newRow)
            out.append(newRow)
        return out
            