from typing import Optional, List
from treenode import TreeNode


class InOrder:
    def __init__(self, tree: Optional[TreeNode]):
        self.tree = tree
        self.traverse = []

    def recursive_lib(self, tree: Optional[TreeNode]):
        if not tree:
            return
        self.recursive_lib(tree.left)
        self.traverse.append(tree.val)
        self.recursive_lib(tree.right)

    def recursive(self) -> List[int]:
        self.recursive_lib(self.tree)
        return self.traverse

    def iterative(self) -> List[int]:
        stack = []
        root = self.tree
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            self.traverse.append(root.val)
            root = root.right

        return self.traverse

    def empty_traversal(self):
        self.traverse = []


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(5)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(7)
    t.left.left.left = TreeNode(8)
    t.left.left.right = TreeNode(9)

    p = InOrder(t)
    print("In Order with Recursion")
    res = p.recursive()
    print(res)

    p.empty_traversal()

    print("In Order without Recursion")
    res = p.iterative()
    print(res)
