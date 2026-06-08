class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {}

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
        for v in count_map:
            if count_map[v] > 0:
                return False
        return True