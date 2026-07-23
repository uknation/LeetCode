class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

############

# counting
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums1 + nums2)
        return [x for x in arr1 if cnt[x] == 2]

############

'''
https://docs.python.org/3/reference/expressions.html#operator-precedence

high to low:

**

*, @, /, //, %

+, -

<<, >>

&

^

|

in, not in, is, is not, <, <=, >, >=, !=, ==

and

or

if – else


'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        res = set()
        for num in nums2:
            if num in s:
                res.add(num)
        return list(res)

############

# no extra space
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # ans.append(nums1[i]) # for Leetcode 350, input with duplicates
                if (not ans) or (len(ans) > 0 and ans[-1] != nums1[i]):
                    ans.append(nums1[i])
                i += 1
                j += 1

        return ans

############

class Solution(object):
  def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = []
    for num in nums1:
      d[num] = d.get(num, 0) + 1

    for num in nums2:
      if num in d:
        ans.append(num)
        del d[num]
    return ans