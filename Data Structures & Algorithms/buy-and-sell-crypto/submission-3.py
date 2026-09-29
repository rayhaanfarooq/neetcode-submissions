class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 0
        profit = float("-inf")

        while r < len(prices):

            price = prices[r] - prices[l]


            if prices[l] > prices[r]:
                l = r

            profit = max(profit, price)
            r += 1

        return profit

            
        