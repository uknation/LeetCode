'''
>>> p = "abba"
>>> s = "dog cat cat dog".split()
>>> s
['dog', 'cat', 'cat', 'dog']
>>> zip(p,s)
[('a', 'dog'), ('b', 'cat'), ('b', 'cat'), ('a', 'dog')]
>>> set(zip(p,s))
set([('b', 'cat'), ('a', 'dog')])
>>>
>>>
>>> s = "dog dog dog dog".split() # then false for: len(set(pattern)) == len(set(str))
>>> zip(p,s)
[('a', 'dog'), ('b', 'dog'), ('b', 'dog'), ('a', 'dog')]
>>> set(zip(p,s))
set([('a', 'dog'), ('b', 'dog')])
'''

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        a = zip(pattern, s)
        return len(pattern) == len(s) and len(set(a)) == len(set(pattern)) == len(set(s))

############

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        n = len(pattern)
        if n != len(s):
            return False
        c2str, str2c = defaultdict(), defaultdict()
        for i in range(n):
            k, v = pattern[i], s[i]
            if k in c2str and c2str[k] != v:
                return False
            if v in str2c and str2c[v] != k:
                return False
            c2str[k], str2c[v] = v, k
        return True