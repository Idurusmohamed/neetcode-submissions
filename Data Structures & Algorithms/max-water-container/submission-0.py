class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res_max = 0

        # my pseudo notes: I need: area, width, height, w * h = Area

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res_max = max(res_max, min(heights[i], heights[j]) * (j - i))
        return res_max