from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables
        min_price = float('inf')  # Set initial min price to infinity
        max_profit = 0  # Initialize max profit to 0
        
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the potential profit
            profit = price - min_price
            # Update max profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

