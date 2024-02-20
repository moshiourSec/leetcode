class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s, reverse=False)
        sorted_t = sorted(t, reverse=False)
        if sorted_s == sorted_t:
            return True
        return False