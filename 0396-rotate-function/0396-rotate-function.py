class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = sum(i * v for i, v in enumerate(nums))
        n, s = len(nums), sum(nums)
        ans = f
        for i in range(1, n): # starting at 1, not 0 which is f
            f = f + s - n * nums[n - i]
            ans = max(ans, f)
        return ans

############

class Solution(object):
  def maxRotateFunction(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    if not A:
      return 0

    sumA = sum(A)
    fk = 0
    n = len(A)
    for i, num in enumerate(A):
      fk += i * num
    idx = n - 1
    ans = float("-inf")
    for _ in range(n):
      fk += sumA - n * A[idx]
      ans = max(ans, fk)
      idx -= 1
    return ans
