# time complexity: O(n)
import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            print("prices[i]=", prices[i])
            print("min_price=", min_price)
            print("max_profit=", max_profit)
            print("-----------------")
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


input = Solution()
print(input.maxProfit([7,6,4,3,1]))