class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = []
        
        for s in A:
            #make 2 dicts for even and odd characters
            even_dct = {}
            odd_dct = {}
            for i in range(len(s)):
                dct = even_dct if i % 2 == 0 else odd_dct
                c = s[i]
                if c not in dct:
                    dct[c] = 1
                else:
                    dct[c] += 1
                
            group_found = False
            for group in groups:
                no_even_mismatch = True
                no_odd_mismatch = True
                even_chars = group[0]
                odd_chars = group[1]
                
                for key in even_dct.keys():
                    #if there's mismatch in dicts, this is not the group for the word
                    if (key not in even_chars) or (even_chars[key] != even_dct[key]):
                        no_even_mismatch = False
                        break
                        
                for key in odd_dct.keys():
                    #if there's mismatch in dicts, this is not the group for the word
                    if (key not in odd_chars) or (odd_chars[key] != odd_dct[key]):
                        no_odd_mismatch = False
                        break 
                        
                if no_even_mismatch and no_odd_mismatch:
                    group_found = True
                    break
                    
            #if at the end there's no group for the word, at its dict as a new group
            if not group_found:
                groups.append((even_dct, odd_dct))
        
        return len(groups)