# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution: # recursion
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        if len(s) <= 2: # '[]'
            return NestedInteger()
        ans = NestedInteger()
        depth, i = 0, 1 # i starting at 1, to skip first '['
        for j in range(1, len(s)):
            if depth == 0 and (s[j] == ',' or j == len(s) - 1):
                ans.add(self.deserialize(s[i:j])) # j at ']', exclusive
                i = j + 1
            elif s[j] == '[':
                depth += 1
            elif s[j] == ']':
                depth -= 1
        return ans

############


'''
If we encounter an opening bracket [
    we push the current nested list onto the stack
    and create a new nested list for the current level.

If we encounter a closing bracket ]
    we add the current number (if any) to the current nested list,
    and if there are elements on the stack, we pop the top nested list from the stack and add the current nested list to it.

If we encounter a comma ,
    we add the current number (if any) to the current nested list.
Otherwise, we append the character to the num string, which represents the number we are currently parsing.
'''
class Solution: # iteration
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return None

        if s[0] != '[':
            return NestedInteger(int(s))

        stack = [] # keep track of nested levels
        curr = None # current nested list that we are constructing
        num = ""
        for char in s:
            if char == '[':
                if curr:
                    stack.append(curr)
                curr = NestedInteger()
            elif char == ']':
                if num:
                    curr.add(NestedInteger(int(num)))
                    num = ""
                if stack:
                    pop_curr = curr
                    curr = stack.pop()
                    curr.add(pop_curr)
            elif char == ',':
                if num:
                    curr.add(NestedInteger(int(num)))
                    num = ""
            else:
                num += char

        return curr
