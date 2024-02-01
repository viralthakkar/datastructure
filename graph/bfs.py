from collections import defaultdict, deque
from typing import List


class BFSTraverse:
    def __init__(self, vertices: int):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u: int, v: int):
        self.graph[u].append(v)

    def traverse(self, u: int) -> List[int]:
        visited = set()

        queue = deque([u])
        visited.add(u)

        traverse_list = []

        while queue:
            vertex = queue.popleft()

            traverse_list.append(vertex)

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

        return traverse_list


if __name__ == '__main__':
    g = BFSTraverse(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    nodes = g.traverse(2)
    print(nodes)