class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        earn = 0
        buy = prices[0]

        for price in prices:
            profit = price - buy
            earn = max(earn, profit)
            buy = min(price, buy)
        return earn            