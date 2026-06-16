class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #initialize two pointers and result of max
        l = 0
        r = len(heights) - 1
        res_max = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res_max = max(res_max, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res_max
