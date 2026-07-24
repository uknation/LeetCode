'''
>>> from itertools import pairwise
>>> dirs = (-1, 0, 1, 0, -1)
>>> pairwise(dirs)
<itertools.pairwise object at 0x104dbe470>
>>> list(pairwise(dirs))
[(-1, 0), (0, 1), (1, 0), (0, -1)]
'''

from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        vis = [[False] * n for _ in range(m)] # visited
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1: # border enqueue
                    heappush(pq, (heightMap[i][j], i, j)) # default order
                    vis[i][j] = True
        ans = 0
        dirs = (-1, 0, 1, 0, -1)
        while pq:
            h, i, j = heappop(pq)
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if x >= 0 and x < m and y >= 0 and y < n and not vis[x][y]:
                    ans += max(0, h - heightMap[x][y]) # look for neighbour which is lower than pop result hight
                    vis[x][y] = True
                    heappush(pq, (max(h, heightMap[x][y]), x, y))
        return ans

############

class Solution(object):
  def trapRainWater(self, heightMap):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    if not heightMap:
      return 0
    h = len(heightMap)
    w = len(heightMap[0])
    ans = 0
    heap = []
    visited = set()
    for j in range(w):
      heapq.heappush(heap, (heightMap[0][j], 0, j))
      heapq.heappush(heap, (heightMap[h - 1][j], h - 1, j))
      visited |= {(0, j), (h - 1, j)}
    for i in range(h):
      heapq.heappush(heap, (heightMap[i][0], i, 0))
      heapq.heappush(heap, (heightMap[i][w - 1], i, w - 1))
      visited |= {(i, 0), (i, w - 1)}
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while heap:
      height, i, j = heapq.heappop(heap)
      for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in visited:
          ans += max(0, height - heightMap[ni][nj])
          heapq.heappush(heap, (max(heightMap[ni][nj], height), ni, nj)) # update new hight, max(heightMap[ni][nj], height)
          visited |= {(ni, nj)}
    return ans