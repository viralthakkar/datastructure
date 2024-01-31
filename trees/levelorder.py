from collections import deque
from typing import Optional, List
from treenode import TreeNode


class LevelOrder:
    def __init__(self, tree: Optional[TreeNode]):
        self.tree = tree
        self.traverse = []

    def iterative(self):
        queue = deque([])
        node = self.tree
        queue.append(node)

        while queue:
            node = queue.popleft()

            self.traverse.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return self.traverse


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

    p = LevelOrder(t)
    print("Level Order")
    res = p.iterative()
    print(res)
