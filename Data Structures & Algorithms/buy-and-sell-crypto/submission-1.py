class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        So basically just look at the analogy behind buying 
        and selling stocks.
        You buy LOW and sell HIGH. So just iterate through the 
        indices in the array similarly until you find an array
        that meets that threshold goal.
        """
        # for each value buy low and sell high
        # Brute force method
        max_profit = 0

        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                current_profit = prices[sell] - prices[buy]
                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
                

        