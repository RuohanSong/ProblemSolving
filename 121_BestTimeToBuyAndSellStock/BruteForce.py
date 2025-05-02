# time complexity: O(n^2)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        # len(prices) - 1 because the buyDay does not need to be the last day
        # when it is the last day, the sell day runs out of the array
        for buyDay in range(len(prices) - 1):
            for sellDay in range(buyDay + 1, len(prices)):
                if prices[sellDay] - prices[buyDay] > maxProfit:
                    maxProfit = prices[sellDay] - prices[buyDay]
        return maxProfit


input = Solution()
print(input.maxProfit([7,6,4,3,1,10]))