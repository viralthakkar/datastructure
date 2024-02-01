from typing import Optional, List
from trees.treenode import TreeNode


class BinarySearchTree:
    def __init__(self, tree: Optional[TreeNode]):
        self.tree = tree

    def bst_recursive(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        if root:
            if root.val == target:
                return True

            if root.val > target:
                return self.bst_recursive(root.left, target)
            else:
                return self.bst_recursive(root.right, target)

    def is_element_present(self, target: int) -> bool:
        root = self.tree

        ans = self.bst_recursive(root, target)

        return ans


if __name__ == '__main__':
    t = TreeNode(8)
    t.left = TreeNode(5)
    t.right = TreeNode(15)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(6)
    t.right.left = TreeNode(14)
    t.right.right = TreeNode(17)
    t.left.left.left = TreeNode(2)
    t.left.left.right = TreeNode(1)
    t.right.right.left = TreeNode(16)
    t.left.left.right = TreeNode(19)

    p = BinarySearchTree(t)
    print(p.is_element_present(3))
    print(p.is_element_present(4))
    print(p.is_element_present(1))
    print(p.is_element_present(16))
    print(p.is_element_present(20))
    print(p.is_element_present(18))
