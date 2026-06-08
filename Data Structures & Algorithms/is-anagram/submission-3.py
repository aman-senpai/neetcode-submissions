class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {}

        if len(s) != len(t):
            return False
        for c in s:
            if c in count_map:
                count_map[c] += 1
                continue
            count_map[c] = 1
        
        for c in t:
            if c not in count_map:
                return False
            if c in count_map:
                if count_map[c] <= 0:
                    return False
                count_map[c] -= 1
                continue
        return True