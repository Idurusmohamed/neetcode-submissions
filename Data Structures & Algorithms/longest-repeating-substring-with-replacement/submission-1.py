class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
        Brute force method
        length of the longest substring which contains 
        only one distinct character (identical letters) """
        #scores the longest valid window
        res = 0

        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res



