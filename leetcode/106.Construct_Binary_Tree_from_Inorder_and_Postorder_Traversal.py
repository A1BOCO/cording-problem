from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        left = self.buildTree(inorder[:index], postorder[:index])
        right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        root.left = left
        root.right = right
        return root

solution = Solution()
solution.buildTree([9,3,15,20,7],[9,15,7,20,3])