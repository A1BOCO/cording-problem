class Solution:
    def isSymmetric(self, root) -> bool:

        def isSymmetricHelper(left, right):

            if not left and not right:
                return True
            if left and not right:
                return False
            if not left and right:
                return False

            left_result = isSymmetricHelper(left.right, right.left)
            right_result = isSymmetricHelper(left.left, right.right)

            if left_result and right_result and left.val == right.val:
                return True
            else:
                return False

        return isSymmetricHelper(root.left, root.right)