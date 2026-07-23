class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f1, f2, f3 = -prices[0], 0, 0
        for price in prices[1:]:
            pf1, pf2, pf3 = f1, f2, f3
            f1 = max(pf1, pf3 - price)
            f2 = max(pf2, pf1 + price)
            f3 = max(pf3, pf2) # cooldown
        return f2

############

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f, f0, f1 = 0, 0, -prices[0]
        for x in prices[1:]:
            f, f0, f1 = f0, max(f0, f1 + x), max(f1, f - x)
        return f0

############

class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
      return 0
    buy = [0] * len(prices)
    sell = [0] * len(prices)
    buy[0] = -prices[0]
    buy[1] = max(-prices[1], buy[0])
    sell[0] = 0
    sell[1] = max(prices[1] - prices[0], 0)
    for i in range(2, len(prices)):
      buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
      sell[i] = max(prices[i] + buy[i - 1], sell[i - 1])
    return max(sell)