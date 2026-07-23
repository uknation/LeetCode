# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# better and easier, manual filter() via while
# I like this one the most
class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, val: int) -> None:
        new_interval = [val, val]
        merged_intervals = []
        i = 0

        # before overlap part
        while i < len(self.intervals) and self.intervals[i][1] < val - 1:
            merged_intervals.append(self.intervals[i])
            i += 1

        # process overlap
        while i < len(self.intervals) and self.intervals[i][0] <= val + 1:
            new_interval[0] = min(new_interval[0], self.intervals[i][0])
            new_interval[1] = max(new_interval[1], self.intervals[i][1])
            i += 1

        merged_intervals.append(new_interval)

        # after overlap part
        while i < len(self.intervals):
            merged_intervals.append(self.intervals[i])
            i += 1

        # also passed OJ, instead of while loop:
        # merged_intervals.extend(self.intervals[i:])

        self.intervals = merged_intervals

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

############

class SummaryRanges: # passed OJ, optimized below solution

  def __init__(self):
    self.intervals = []

  def insert(self, newInterval: List[int]):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    intervals = self.intervals
    # print intervals
    if not intervals:
      intervals.append(newInterval)
      return

    s, e = newInterval[0], newInterval[1]
    left = list(filter(lambda x: x[1] + 1 < newInterval[0], intervals))
    right = list(filter(lambda x: x[0] - 1 > newInterval[1], intervals))

    if left + right != intervals:
      s = min(intervals[len(left)][0], s)
      e = max(intervals[~len(right)][1], e)

    # +1 or -1 check: included in lambda's '+1<' and '-1>'
    self.intervals = left + [ [s, e] ] + right

  def addNum(self, val: int) -> None:
    self.insert([val, val])

  def getIntervals(self) -> List[List[int]]:

    return self.intervals


############


class SummaryRanges: # above is optimized version

  def __init__(self):
    self.intervals = []

  def insert(self, newInterval: List[int]):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    intervals = self.intervals
    # print intervals
    if not intervals:
      intervals.append(newInterval)
      return
    s, e = newInterval[0], newInterval[1]
    left = list(filter(lambda x: x[1] < newInterval[0], intervals))
    right = list(filter(lambda x: x[0] > newInterval[1], intervals))
    # print left, right, (s, e)
    if left + right != intervals:
      s = min(intervals[len(left)][0], s)
      e = max(intervals[~len(right)][1], e)
    newIntv = [s, e]

    # merging piece is different from above solution
    if left and left[-1][1] + 1 == s:
      newIntv[0] = left[-1][0]
      left = left[:-1]  # cut out last one, which is merged with newIntv
    if right and right[0][0] - 1 == e:
      newIntv[1] = right[0][1]
      right = right[1:]  # cut out first one, which is merged with newIntv
    self.intervals = left + [newIntv] + right

  def addNum(self, val: int) -> None:
    self.insert([val, val])

  def getIntervals(self) -> List[List[int]]:

    return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


############

'''
>>> mp = SortedDict()
>>> mp.bisect_right(3)
0


>>> mp = SortedDict()
>>> mp[1]=[1,1]
>>> mp[3]=[3,3]
>>> mp[5]=[5,5]
>>>
>>> mp
SortedDict({1: [1, 1], 3: [3, 3], 5: [5, 5]})
>>> mp.bisect_right(-10)
0
>>> mp.bisect_right(100)
3
>>> mp.bisect_right(2)
1
>>> mp.values()
SortedValuesView(SortedDict({1: [1, 1], 3: [3, 3], 5: [5, 5]}))
>>> list(mp.values())
[[1, 1], [3, 3], [5, 5]]
>>>
'''
from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self):
        self.mp = SortedDict()

    def addNum(self, val: int) -> None:
        n = len(self.mp)
        ridx = self.mp.bisect_right(val)
        lidx = n if ridx == 0 else (ridx - 1) # n is similar to java treemap returning null
        keys = self.mp.keys()
        values = self.mp.values()
        if (
            lidx != n
            and ridx != n
            and values[lidx][1] + 1 == val
            and values[ridx][0] - 1 == val
        ):
            self.mp[keys[lidx]][1] = self.mp[keys[ridx]][1]
            self.mp.pop(keys[ridx])
        elif lidx != n and val <= values[lidx][1] + 1: # <= because, it could be [1 -> 10], and new add is [5,5]
            self.mp[keys[lidx]][1] = max(val, self.mp[keys[lidx]][1])
        elif ridx != n and val >= values[ridx][0] - 1:
            self.mp[keys[ridx]][0] = min(val, self.mp[keys[ridx]][0])
        else:
            self.mp[val] = [val, val]

    def getIntervals(self) -> List[List[int]]:
        return list(self.mp.values())


# # Your SummaryRanges object will be instantiated and called as such:
# # obj = SummaryRanges()
# # obj.addNum(val)
# # param_2 = obj.getIntervals()