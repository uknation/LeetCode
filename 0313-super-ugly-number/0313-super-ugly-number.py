'''
The time complexity of the provided code is `O(n * k * log(n))`
* where n is the input parameter n.
* where k is the number of prime numbers in the input list

    For a single outer for loop iteration
        * Popping the smallest element from the heap using heappop(), which takes `O(log(n))` time complexity.
        * Pushing the new number into the heap using heappush(), which takes `O(log(n))` time complexity.
        * Therefore, the overall time complexity of the loop is `O(k * log(n))`, where k is the number of prime numbers in the input list.

    Since the loop runs for n iterations and each iteration has a time complexity of O(k * log(n)), the total time complexity of the code is `O(n * k * log(n))`.


The space complexity of the code is `O(n)` due to the heap and the hash table
* where n is the input parameter n.
'''

from heapq import heappush, heappop

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        h = [1] # heap
        vis = {1} # hashtable to de-dup
        ans = 1 # initiator
        for _ in range(n):
            ans = heappop(h)
            for v in primes:
                nxt = ans * v
                if nxt not in vis:
                    vis.add(nxt)
                    heappush(h, nxt)
        return ans


############

'''
>>> a = {x:x+1 for x in range(10)}
>>> a
{0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
>>> a.items()
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
>>> a.values()
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.keys()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> float("-inf") == -math.inf
True
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n <= 0 or primes is None:
            return 0

        nums = [1]
        index = [0] * len(primes)

        while len(nums) < n:
            minv = float('inf')
            for i in range(len(primes)):
                minv = min(minv, primes[i] * nums[index[i]])
            nums.append(minv)

            for i in range(len(primes)):
                if primes[i] * nums[index[i]] == minv:
                    index[i] += 1

        return nums[-1]

if __name__ == '__main__':
    # if no de-dup, result will be:
    #           [1, 2, 4, 7, 8, 13, 14, 14, 16, 19, 26, 26]
    # corret:   [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
    print(Solution().nthSuperUglyNumber(12, [2,7,13,19]))

#############

class Solution: # not that good, just for reference
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        x = 0
        mx_int = (1 << 31) - 1
        for _ in range(n):
            x = heappop(q)
            for k in primes:
                if x <= mx_int // k: # make sure not overflow int type
                    heappush(q, k * x)
                if x % k == 0: # to avoid duplicates, eg [2,3,5], when x is 6
                    break
            # print(x)
            # print(list(q))
        return x

'''
primes = [2,3,5]
n = 10
result should be: 12
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]


for the print enabled, I got:

    1
    [2, 3, 5]
    2
    [3, 5, 4] ==> heappop got 3, 3%3==0 so still added 3*3=9, but not added 3*5=15
    3
    [4, 5, 6, 9]
    4
    [5, 8, 6, 9]
    5
    [6, 8, 9, 10, 15, 25]
    6
    [8, 10, 9, 25, 15, 12]
    8
    [9, 10, 12, 25, 15, 16]
    9
    [10, 15, 12, 25, 16, 18, 27]
    10
    [12, 15, 18, 25, 16, 27, 20]
    12
    [15, 16, 18, 25, 20, 27, 24]
'''