class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookies = sorted(s)
        greeds = sorted(g)
        
        cur_cookie_pos = 0
        
        for i in range(len(greeds)):
            greed = greeds[i]
            cookie_found = False
            while cur_cookie_pos < len(cookies):
                cookie = cookies[cur_cookie_pos]
                cur_cookie_pos += 1
                if greed <= cookie:
                    cookie_found = True
                    break
                
            if not cookie_found:
                return i
            
        return len(greeds)