class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l = buy, r = sell
        max_prof = 0

        while r < len(prices):
            if prices[l] < prices[r]: #profitability check
                profit = prices[r] - prices[l]
                max_prof = max(max_prof, profit)
            else:
                l = r
            r += 1
        return max_prof