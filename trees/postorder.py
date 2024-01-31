from typing import Optional, List
from treenode import TreeNode


class PostOrder:
    def __init__(self, tree: Optional[TreeNode]):
        self.tree = tree
        self.traverse = []

    def recursive_lib(self, tree: Optional[TreeNode]):
        if not tree:
            return
        self.recursive_lib(tree.left)
        self.recursive_lib(tree.right)
        self.traverse.append(tree.val)

    def recursive(self) -> List[int]:
        self.recursive_lib(self.tree)
        return self.traverse

    def iterative(self) -> List[int]:
        node = self.tree
        visited = set()
        stack = []

        while stack or node:
            while node and node not in visited:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                self.traverse.append(node.val)
                node = None

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

    p = PostOrder(t)
    print("Post Order with Recursion")
    res = p.recursive()
    print(res)

    p.empty_traversal()

    print("Post Order without Recursion")
    res = p.iterative()
    print(res)
