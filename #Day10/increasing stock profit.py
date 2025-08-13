class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')  # Start with a very high number
        max_profit = 0
        
        for price in prices:
            # Update min price if a lower one is found
            if price < min_price:
                min_price = price
            
            # Calculate profit if selling today
            profit = price - min_price
            
            # Update max profit if this profit is higher
            if profit > max_profit:
                max_profit = profit
        
        return max_profit


# Example run
prices = [7,1,5,3,6,4]
result = Solution().maxProfit(prices)
print("Max profit:", result)