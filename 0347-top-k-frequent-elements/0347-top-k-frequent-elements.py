'''
>>> nums = ["a", "a", "b", "c", "c"]

>>> cnt = Counter(nums)
>>> cnt
Counter({'a': 2, 'c': 2, 'b': 1})

# default to keys
>>> sorted_freqs = sorted(cnt, key=lambda x: (-cnt[x], x))
>>> sorted_freqs
['a', 'c', 'b']
'''
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in the list
        cnt = Counter(nums)

        # Sort the elements by frequency in decreasing order
        # diff from below solution: sorted(cnt), not sorted(cnt.items())
        #   more in https://leetcode.ca/2017-10-22-692-Top-K-Frequent-Words/
        sorted_freqs = sorted(cnt, key=lambda x: (-cnt[x], x))

        return sorted_freqs[:k]

##############

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in the list
        freqs = Counter(nums)

        # Sort the elements by frequency in decreasing order
        sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        # also passing OJ: sorted_freqs = sorted(freqs.items(), key=lambda x: -x[1])

        # Take the top k elements
        top_k = [num for num, freq in sorted_freqs[:k]]

        return top_k

##############

'''
>>> from heapq import heappush
>>> h = []
>>> heappush(h, (3,1))
>>> heappush(h, (1,1))
>>> heappush(h, (2,1))
>>> h
[(1, 1), (3, 1), (2, 1)]

>>> from heapq import heappop
>>> heappop(h)
(1, 1)
>>> heappop(h)
(2, 1)
>>> heappop(h)
(3, 1)
'''

from collections import Counter

class Solution: # heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        hp = []
        for num, freq in cnt.items():
            heappush(hp, (freq, num)) # freq first, default sort by 1st element
            if len(hp) > k:
                heappop(hp)
        return [v[1] for v in hp]

##############

from typing import List
import random
# O(n log(n)) in the average case
# O(n^2) worst case
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        freq_list = list(freq_map.items())
        self.quick_select(freq_list, 0, len(freq_list) - 1, k)

        return [num for num, freq in freq_list[:k]]

    def quick_select(self, freq_list, start, end, k):
        if start == end:
            return

        pivot_idx = random.randint(start, end)
        pivot_freq = freq_list[pivot_idx][1]

        left = start
        right = end

        while left <= right:
            while freq_list[left][1] > pivot_freq:
                left += 1
            while freq_list[right][1] < pivot_freq:
                right -= 1

            if left <= right:
                freq_list[left], freq_list[right] = freq_list[right], freq_list[left]
                left += 1
                right -= 1

        if k <= right:
            self.quick_select(freq_list, start, right, k)
        elif k >= left:
            self.quick_select(freq_list, left, end, k)


###########


'''
>>> x = [1, 2, 3]
>>> x.append([4, 5])
>>> print(x)
[1, 2, 3, [4, 5]]


>>> x = [1, 2, 3]
>>> x.extend([4, 5])
>>> print(x)
[1, 2, 3, 4, 5]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        # not always filled, max possible frequency is len(nums) [1,1,1,1,...]
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq.items():
            buckets[freq].append(num)

        res = []
        for bucket in reversed(buckets):
            if bucket:
                res.extend(bucket)
                if len(res) >= k:
                    break

        return res[:k]

############

class Solution(object):
  def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = {}
    res = []
    ans = []
    buckets = [[] for _ in range(len(nums) + 1)]

    for num in nums:
      d[num] = d.get(num, 0) + 1

    for key in d:
      res.append((d[key], key))

    for t in res:
      freq, key = t
      buckets[freq].append(key)

    buckets.reverse()

    for item in buckets:
      if item and k > 0:
        while item and k > 0:
          ans.append(item.pop())
          k -= 1
        if k == 0:
          return ans

    return ans
