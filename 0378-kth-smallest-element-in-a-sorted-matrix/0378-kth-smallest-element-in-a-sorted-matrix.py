'''
time complexity of the countSmallerThanMid(mid) function is O(n), 
as it iterates through at most n rows and columns of the matrix.

number of iterations in the binary search `while left < right:` 
is O(log(maxVal - minVal)), where maxVal - minVal represents the range of values in the matrix.

overall time complexity of the code is `O(n * log(maxVal - minVal))`

no extra space
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countSmallerThanMid(mid):
            count = 0
            # start from top-right corner, where all its left is smaller but all its below is larger
            i, j = 0, n - 1 
            while i < n and j >= 0:
                if matrix[i][j] > mid:
                    j -= 1
                else:
                    count += j + 1 # j is index, j+1 is count for that row
                    i += 1
            return count

        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        while left < right:
            mid = (left + right) >> 1
            if countSmallerThanMid(mid) >= k:
                # The kth smallest element is smaller than or equal to mid, so update the right boundary
                right = mid
            else:
                # The kth smallest element is larger than mid, so update the left boundary
                left = mid + 1
        # If the loop terminates, left and right will be equal
        # Return left (or right), which represents the kth smallest element
        return left
        # also passing OJ: return right


############

'''
This algorithm runs in O(n) time complexity 
because each every element is added to the heap only once and is visited only once

The space complexity is also O(n) 
because we store at most n elements in the heap and at most n elements in the visited set
'''
import heapq

class Solution(object):
  def kthSmallest(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    visited = {(0, 0)}
    heap = [(matrix[0][0], (0, 0))]

    while heap: # checking every element
      val, (i, j) = heapq.heappop(heap)
      k -= 1
      if k == 0:
        return val
      if i + 1 < len(matrix) and (i + 1, j) not in visited:
        heapq.heappush(heap, (matrix[i + 1][j], (i + 1, j)))
        visited.add((i + 1, j))
      if j + 1 < len(matrix[0]) and (i, j + 1) not in visited:
        heapq.heappush(heap, (matrix[i][j + 1], (i, j + 1)))
        visited.add((i, j + 1))
