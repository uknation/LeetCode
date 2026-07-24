from collections import defaultdict
from random import choice

class RandomizedCollection: # official solution

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.dict = defaultdict(set) # change from 381 (with no duplicates)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.dict[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.dict[val]) == 1


    '''
        >>> a = set([1,1,2,3])
        >>> a
        {1, 2, 3}
        >>> a.pop()
        1
        >>> a
        {2, 3}
    '''
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.dict[val]:
            return False
        remove_index, last_val = self.dict[val].pop(), self.lst[-1] # pop() on a set
        self.lst[remove_index] = last_val
        self.dict[last_val].add(remove_index)
        self.dict[last_val].discard(len(self.lst) - 1)

        self.lst.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.lst)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()