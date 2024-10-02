"""
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        First set the buy price to day 1, 
        keep going through the array,
        find the day where the sell_price is lesser than buy_price, 
        set that as the new buy price and continue.
        Calculate the max_profit at every stage
        Time: O(1)
        Space: O(1)
        """
        if not prices or len(prices)<=1:
            return 0
        max_profit = 0
        buy_price = prices[0]
        for sell_price in prices[1:]:
            current_profit = sell_price - buy_price
            max_profit = max(max_profit, current_profit)
            if buy_price > sell_price:
                buy_price = sell_price
        return max_profit
