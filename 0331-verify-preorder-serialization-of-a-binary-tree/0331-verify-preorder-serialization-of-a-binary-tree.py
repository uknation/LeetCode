'''
In this solution, we split the input string by comma to get a list of nodes. 
We then initialize the indegree counter to 1 for the root node, 
since the root has no incoming edges.

We then loop through the nodes and for each node, we decrease the indegree counter by 1. 
If the indegree counter becomes negative, 
it means that there are more incoming edges than expected, 
and the tree is invalid. In this case, we return False.

If the current node is not null (i.e., not '#'), 
we increase the indegree counter by 2 for its two children. 
This is because every non-null node has two children in a binary tree. 
Finally, we return True if the final indegree counter is 0, 
meaning that all incoming edges have been accounted for.
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Split the string by comma to get the list of nodes
        nodes = preorder.split(',')

        # since the root has no incoming edges
        indegree = 1

        for node in nodes:
            # Decrease the indegree for the current node
            indegree -= 1

            # If the indegree is negative, return False because the tree is invalid
            if indegree < 0:
                return False

            # If the current node is not null, increase the indegree by 2 for its children
            if node != '#':
                indegree += 2

        # Return True if the final indegree is 0
        return indegree == 0

############

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return True
        
        nodes = preorder.split(",")
        stack = []
        
        for node in nodes:
            if node == "#":
                # after first while loop, current node can be deemed as #
                while stack and stack[-1] == "#":
                    stack.pop() # pop # in stack
                    if not stack: # should leave a number in stack
                        return False
                    
                    stack.pop() # pop val with left-# and right-#   =>   repalce it with #
            stack.append(node)
        
        return len(stack) == 1 and stack[0] == "#"

############

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stk = []
        for c in preorder.split(","):
            stk.append(c)
            while len(stk) > 2 and stk[-1] == stk[-2] == "#" and stk[-3] != "#":
                stk = stk[:-3]
                stk.append("#")
        return len(stk) == 1 and stk[0] == "#"