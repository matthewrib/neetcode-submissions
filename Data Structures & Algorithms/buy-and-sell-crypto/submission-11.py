class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minDay = float("inf")
        maxProfit = 0
        for price in prices:
            if price < minDay:
                minDay = price
            else:
                profit = price - minDay
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit

