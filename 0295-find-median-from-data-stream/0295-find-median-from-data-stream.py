from heapq import heappush, heappop

class MedianFinder:

	def __init__(self):
        # the smaller half of the list, max heap (invert min-heap)
		self.smallerHalf = []
        # the larger half of the list, min heap
		self.largerHalf = []

	def addNum(self, num: int) -> None:

		# trick for smaller half, use -1*val
		# heapq in python does NOT have comparator like in Java
		heappush(self.smallerHalf, -num)
		heappush(self.largerHalf, -heappop(self.smallerHalf)) # note: not self.smallerHalf.pop()

		if len(self.smallerHalf) < len(self.largerHalf):
			heappush(self.smallerHalf, -heappop(self.largerHalf))

	def findMedian(self) -> float:
		if len(self.smallerHalf) == len(self.largerHalf):
			return (-self.smallerHalf[0] + self.largerHalf[0]) / 2.0
		else:
			return float(-self.smallerHalf[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# follow up
class MedianFinder:
    def __init__(self):
        self.counts = [0] * 101
        self.total = 0

    def addNum(self, num: int) -> None:
        self.counts[num] += 1
        self.total += 1

    def findMedian(self) -> float:
        if self.total % 2 == 0:
            # even number of elements
            middle1 = self.total // 2
            middle2 = middle1 + 1
            count = 0
            i1 = i2 = 0
            for i in range(101):
                count += self.counts[i]
                if count >= middle1 and i1 == 0:
                    i1 = i
                if count >= middle2:
                    i2 = i
                    break
            return (i1 + i2) / 2
        else:
            # odd number of elements
            middle = self.total // 2 + 1
            count = 0
            for i in range(101):
                count += self.counts[i]
                if count >= middle:
                    return i


############

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        heappush(self.h1, num)
        heappush(self.h2, -heappop(self.h1))
        if len(self.h2) - len(self.h1) > 1:
            heappush(self.h1, -heappop(self.h2))

    def findMedian(self) -> float:
        if len(self.h2) > len(self.h1):
            return -self.h2[0]
        return (self.h1[0] - self.h2[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()