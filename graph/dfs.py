from collections import defaultdict
from typing import List, Optional, Any


class DFSTraverse:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u: Optional[Any], v: Optional[Any]):
        self.graph[u].append(v)

    def recursive_utils(self, start: int, visited: set, traverse_list: List):
        visited.add(start)
        traverse_list.append(start)

        for neighbour in self.graph[start]:
            if neighbour not in visited:
                visited.add(neighbour)
                self.recursive_utils(neighbour, visited, traverse_list)

    def recursive(self, start: any):
        visited = set()
        traverse_list = []

        self.recursive_utils(start, visited, traverse_list)

        return traverse_list

    def traverse(self, start: any) -> List[Any]:
        visited = set()
        traverse_list = []

        stack = [start]
        visited.add(start)

        while stack:
            vertex = stack.pop()

            traverse_list.append(vertex)

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)

        return traverse_list


if __name__ == '__main__':
    print("Following is Depth First Traversal \n")
    g = DFSTraverse(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    nodes = g.recursive(2)
    print(nodes)

    # graph = [
    #     [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 1]
    # ]
    # g1 = DFSMatrix(graph)
    # g1.dfs(2)
    # print(g1.nodes)

    s = DFSTraverse(7)
    s.add_edge('C', 'A')
    s.add_edge('C', 'F')
    s.add_edge('A', 'B')
    s.add_edge('A', 'D')
    s.add_edge('D', 'F')
    s.add_edge('D', 'G')
    s.add_edge('E', 'G')
    s.add_edge('B', 'D')
    s.add_edge('B', 'E')
    s.add_edge('G', 'F')
    nodes = s.traverse('C')
    print(nodes)
