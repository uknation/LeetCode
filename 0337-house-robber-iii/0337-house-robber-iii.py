class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root, True), self.dfs(root, False))

    # if no cache, then running time over limit
    @cache
    def dfs(self, root: TreeNode, isCurrentRootRobbed: bool) -> int:
        if not root:
            return 0

        if isCurrentRootRobbed:
            return root.val + self.dfs(root.left, False) + self.dfs(root.right, False)
        else:
            return self.rob(root.left) + self.rob(root.right)
            # below else logic also passing OJ
            # return max(self.dfs(root.left, True), self.dfs(root.left, False)) + max(self.dfs(root.right, True), self.dfs(root.right, False))

###########

# better and concise
class Solution: # post-order
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left, right = dfs(node.left), dfs(node.right)
            rob = node.val + left[1] + right[1] # [1] meaming left/right children skippted
            skip = max(left) + max(right)
            return rob, skip
        return max(dfs(root))


###########


class Solution: # return in else is too lengthy...
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root, True), self.dfs(root, False))

    # if no cache, then running time over limit
    @cache
    def dfs(self, root: TreeNode, isCurrentRootRobbed: bool) -> int:
        if not root:
            return 0

        if isCurrentRootRobbed:
            return root.val + self.dfs(root.left, False) + self.dfs(root.right, False)
        else:
            return max(self.dfs(root.left, True), self.dfs(root.left, False)) + max(self.dfs(root.right, True), self.dfs(root.right, False))
