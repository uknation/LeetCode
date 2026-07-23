'''
>>> nums = list(range(1,11))
>>> nums
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> nums[::2]
[1, 3, 5, 7, 9]
>>> nums[1::2]
[2, 4, 6, 8, 10]
>>>
>>> mid = (len(nums) - 1) // 2
>>> mid
4
>>> nums[mid::-1]
[5, 4, 3, 2, 1]
>>> nums[:mid:-1]
[10, 9, 8, 7, 6]
>>>
>>> nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
>>> nums
[5, 10, 4, 9, 3, 8, 2, 7, 1, 6]
>>>
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        mid = (n - 1) // 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]

        # better to have descending list, below having error
        #   input: [4,5,5,6], below line output: [4,5,5,6]
        # nums[::2], nums[1::2] = nums[:mid+1:1], nums[mid+1::1]
        '''
        >>> nums=[4,5,5,6]
        >>> mid = (len(nums) - 1) // 2
        >>>
        >>> nums[::2]
        [4, 5]
        >>> nums[1::2]
        [5, 6]
        >>> nums[mid::-1]
        [5, 4]
        >>> nums[:mid:-1]
        [6, 5]
        >>> nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
        >>> nums
        [5, 6, 4, 5]
        '''
class Solution: # extra space
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums) # extra O(N) space
        n = len(arr)
        i, j = (n - 1) >> 1, n - 1
        for k in range(n):
            if k % 2 == 0:
                nums[k] = arr[i]
                i -= 1
            else:
                nums[k] = arr[j]
                j -= 1

class Solution: # quicksort, without full sort
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        
        mid = self.findKthLargest(nums, (n + 1) // 2)
        
        def idx(i):
            return (2 * i + 1) % (n | 1)
        
        i, j, k = 0, 0, n - 1
        while j <= k:
            if nums[idx(j)] > mid:
                nums[idx(i)], nums[idx(j)] = nums[idx(j)], nums[idx(i)]
                i += 1
                j += 1
            elif nums[idx(j)] < mid:
                nums[idx(j)], nums[idx(k)] = nums[idx(k)], nums[idx(j)]
                k -= 1
            else:
                j += 1
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while True:
            pivotIdx = self.partition(nums, left, right)
            if pivotIdx == k - 1:
                return nums[pivotIdx]
            elif pivotIdx < k - 1:
                left = pivotIdx + 1
            else:
                right = pivotIdx - 1
    
    def partition(self, nums, left, right):
        pivot = nums[left]
        l, r = left + 1, right
        
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] >= pivot:
                l += 1
            else:
                r -= 1
        
        nums[left], nums[r] = nums[r], nums[left]
        return r