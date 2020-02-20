class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = set()
        
        for word in words:
            morse_code = []
            for c in word:
                i = ord(c) - 97
                morse_code.append(morse[i])
            trans.add(''.join(morse_code))
            
        return len(trans)