class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0

        nums = [1]
        i2, i3, i5 = 0, 0, 0

        while len(nums) < n:
            m2 = nums[i2] * 2
            m3 = nums[i3] * 3
            m5 = nums[i5] * 5

            mn = min(m2, m3, m5)
            nums.append(mn)

            if mn == m2:
                i2 += 1
            if mn == m3:  # Note: 3*2 and 2*3 are both 6, so cannot use elif
                i3 += 1
            if mn == m5:
                i5 += 1
        return nums[-1]

############
from heapq import heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1] # heap
        vis = {1} # hashtable to de-dup
        ans = 1
        for _ in range(n):
            ans = heappop(h)
            for v in [2, 3, 5]:
                nxt = ans * v
                if nxt not in vis:
                    vis.add(nxt)
                    heappush(h, nxt)
        return ans

############

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        p2 = p3 = p5 = 0
        for i in range(1, n):
            next2, next3, next5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(next2, next3, next5)
            if dp[i] == next2:
                p2 += 1
            if dp[i] == next3:
                p3 += 1
            if dp[i] == next5:
                p5 += 1
        return dp[n - 1]

############

class Solution(object):
  def nthUglyNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    i2 = i3 = i5 = 1
    for i in range(2, n + 1):
      dp[i] = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
      if dp[i] == dp[i2] * 2:
        i2 += 1
      if dp[i] == dp[i3] * 3:
        i3 += 1
      if dp[i] == dp[i5] * 5:
        i5 += 1
    return dp[-1]