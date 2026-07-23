'''
>>> from itertools import accumulate
>>> accumulate([1,2,3])
<itertools.accumulate object at 0x108f38340>
>>> list(accumulate([1,2,3]))
[1, 3, 6]
>>> list(accumulate([1,2,3], initial=0))
[0, 1, 3, 6]
>>> list(accumulate([1,2,3], initial=10))
[10, 11, 13, 16]
'''
# note: when using python2, I always got error when importing it, via itertools.accumulate()
#       switching to python3, then all good for itertools.accumulate()
class NumArray:
    def __init__(self, nums: List[int]):
        self.s = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

############

class NumArray(object):
  def __init__(self, nums):
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    self.dp = [0] * (len(nums) + 1)
    for i in range(0, len(nums)):
      self.dp[i + 1] = self.dp[i] + nums[i]

  def sumRange(self, i, j):
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    return self.dp[j + 1] - self.dp[i]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)