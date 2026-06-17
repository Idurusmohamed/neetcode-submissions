class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # Buy pointer
        max_prof = 0

        #the r/sell pointer will be auto handled by range in for loop
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_prof = max(max_prof, profit)
            else:
                l = r # Move buy pointer to current low price
        return max_prof