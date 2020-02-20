import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = collections.Counter()
        
        for cpdomain in cpdomains:
            lst = cpdomain.split(" ")
            count = int(lst[0])
            domain = lst[1]
            
            dct = {}
            dct[domain] = count
            while '.' in domain:
                _, domain = domain.split('.', 1)
                dct[domain] = count
            
            c.update(dct)
            
        out = [] 
        for k, v in c.items():
            out.append(str(v) + " " + k)
            
        return out