# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def setChilds(self, l, nodeIndex):
        leftChildIndex = 2*nodeIndex + 1
        rightChildIndex = 2*nodeIndex + 2
        if(len(l) <= 2*nodeIndex+1):
            return
        if(l[leftChildIndex] is not None):
            self.left = TreeNode(l[leftChildIndex])
            self.left.setChilds(l, leftChildIndex)
        if(l[rightChildIndex] is not None):
            self.right = TreeNode(l[rightChildIndex])
            self.right.setChilds(l, rightChildIndex)

class Solution:
    paths = []
    def maxPathSum(self, root):
        self.paths = []
        self.getPath(root)
        return max(self.paths)
    
    def getPath(self, node):
        leftChildPath = 0
        if(node.left is not None):
            leftChildPath = self.getPath(node.left)
        
        rightChildPath = 0
        if(node.right is not None):
            rightChildPath = self.getPath(node.right)
        
        maxPath = max([
            node.val+rightChildPath,
            node.val+leftChildPath,
            node.val+rightChildPath+leftChildPath,
            node.val
        ])
        self.paths.append(maxPath)

        return max([
            node.val+rightChildPath,
            node.val+leftChildPath,
            node.val
        ])

    def test(self, l):
        rootIndex = 0
        val = l[rootIndex]
        node = TreeNode(val)
        node.setChilds(l, rootIndex)
        return self.maxPathSum(node)

solution = Solution()
print(solution.test([0]))