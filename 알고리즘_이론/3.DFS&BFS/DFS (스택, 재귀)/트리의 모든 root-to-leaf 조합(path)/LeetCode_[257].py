# Definition for a binary tree node.
# 핵심은 Path가 매개변수로 들어간다는 것 !!

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.output = []
        
    def dfs(self, root, path, output):
        if not root:
            return
        if not root.left and not root.right:
            path+=str(root.val)
            output.append(path)
        if root.left:
            self.dfs(root.left, path+str(root.val)+"->", output)
        if root.right:
            self.dfs(root.right, path+str(root.val)+"->", output)
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        self.dfs(root, "" , self.output)
        
        return self.output
        