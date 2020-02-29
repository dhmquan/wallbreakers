class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        denoms = [20, 10, 5]
        in_hand = {}
        for d in denoms:
            in_hand[d] = 0
            
        for bill in bills:
            change_needed = bill - 5
            
            while change_needed != 0:
                change_found = False
                for d in denoms:
                    if d > change_needed or in_hand[d] == 0:
                        continue
                    in_hand[d] -= 1
                    change_needed -= d
                    change_found = True
                    
                if not change_found:
                    return False
                
            in_hand[bill] += 1
            
        return True