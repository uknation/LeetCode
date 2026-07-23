'''
my_dict.pop('b') # vs del d[k]

    my_dict = {'a': 1, 'b': 2, 'c': 3}
    val = my_dict.pop('b')
    print(my_dict)  # {'a': 1, 'c': 3}
    print(val)  # 2

    >>> item = my_dict.pop()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: pop expected at least 1 argument, got 0

    >>> my_dict = {'a': 1, 'b': 2, 'c': 3}
    >>> del my_dict['b']
    >>> my_dict
    {'a': 1, 'c': 3}
'''

from collections import defaultdict
from random import choice

class RandomizedSet(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """

    # value (map) -> its index -> value (list)
    self.d = {}
    self.a = [] # introduce it purely for random

  def insert(self, val):
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    if val in self.d:
      return False
    self.a.append(val)
    self.d[val] = len(self.a) - 1
    return True

  def remove(self, val):
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: int
    :rtype: bool
    """
    if val not in self.d:
      return False
    index = self.d[val]

    # process last index/val
    self.a[index] = self.a[-1]
    self.d[self.a[-1]] = index

    # process to be deleted index/val
    self.a.pop() # delete in list
    del self.d[val] # delete in dict
    # or, self.d.pop(val)
    return True

  def getRandom(self):
    """
    Get a random element from the set.
    :rtype: int
    """
    return self.a[random.randrange(0, len(self.a))]
    # return random.choice(self.a)

############

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
>>> import random
>>> random.choice([1,2,3,4,5])
3
>>> random.choice([1,2,3,4,5])
4
>>> random.choice([1,2,3,4,5])
4
'''
class RandomizedSet:
    def __init__(self):
        self.m = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        self.m[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        idx = self.m[val]
        self.l[idx] = self.l[-1]
        self.m[self.l[-1]] = idx
        self.l.pop()
        self.m.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()