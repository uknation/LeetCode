'''
>>> s = "ababbc"
>>> set(s)
{'b', 'a', 'c'}

>>> s.count('a')
2
>>> s.count('b')
3

>>> s.split('a')
['', 'b', 'bbc']
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            # no need to try all chars with count<k, get the 1st one and return
            if s.count(c) < k: # @note: This character must not appear in any substring
                return max([self.longestSubstring(t, k) for t in s.split(c)])
        return len(s)

class Solution: # iterative, OJ passed
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        result = 0

        # Iterate over the possible values of unique characters in the substring
        for num_unique in range(1, 27):
            freq_map = [0] * 26
            left = 0
            num_chars = 0
            num_chars_at_least_k = 0

            # Sliding window approach to find the longest substring with num_unique characters
            for right in range(n):
                if freq_map[ord(s[right]) - ord('a')] == 0:
                    num_chars += 1
                freq_map[ord(s[right]) - ord('a')] += 1
                if freq_map[ord(s[right]) - ord('a')] == k:
                    num_chars_at_least_k += 1

                # Shrink the window if the number of unique characters exceeds num_unique
                while num_chars > num_unique:
                    freq_map[ord(s[left]) - ord('a')] -= 1
                    if freq_map[ord(s[left]) - ord('a')] == k - 1:
                        num_chars_at_least_k -= 1
                    if freq_map[ord(s[left]) - ord('a')] == 0:
                        num_chars -= 1
                    left += 1

                # Check if all characters in the substring occur at least k times
                if num_chars == num_chars_at_least_k:
                    result = max(result, right - left + 1)

        return result

############

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(l, r):
            cnt = Counter(s[l : r + 1])
            split = next((c for c, v in cnt.items() if v < k), '')
            if not split:
                return r - l + 1
            i = l
            ans = 0
            while i <= r:
                while i <= r and s[i] == split:
                    i += 1
                if i >= r:
                    break
                j = i
                while j <= r and s[j] != split:
                    j += 1
                t = dfs(i, j - 1)
                ans = max(ans, t)
                i = j
            return ans

        return dfs(0, len(s) - 1)