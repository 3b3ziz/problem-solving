from __future__ import annotations

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min, maxProfit = prices[0], 0
        for p in prices:
            _min = min(_min, p)
            diff = p - _min
            if diff > 0 and diff > maxProfit:
                maxProfit = diff
        return maxProfit
        # Sliding window
        # maxProfit = 0
        # i, j = 0, 0
        # minBuy = float("inf")
        # maxSell = float("-inf")
        # for c in range(len(prices)):
        #     if prices[c] < minBuy:
        #         i, j = c, c
        #         minBuy, maxSell = prices[c], prices[c]
        #     if prices[c] > maxSell:
        #         j = c
        #         maxSell = prices[c]
        #     if j > i and maxSell > minBuy and maxSell - minBuy > maxProfit:
        #         maxProfit = maxSell - minBuy
        # return maxProfit 
        # maxProfit = 0

        # n2
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         diff = prices[j] - prices[i]
        #         if diff > maxProfit:
        #             maxProfit = diff
        # return maxProfit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([7,2,5,3,6,1,9]))
print(s.maxProfit([3,2,6,5,0,3]))

