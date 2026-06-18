class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = dict(Counter(sorted(s)))
        freq_b = dict(Counter(sorted(t)))
        
        if len(s) == len(t) and freq_s == freq_b:
            unique_s = list(set(s))
            unique_t = list(set(t))
            return sorted(unique_s) == sorted(unique_t)
        else:
            return False

        