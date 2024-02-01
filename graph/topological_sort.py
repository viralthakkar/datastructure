from collections import defaultdict, deque


class TopologicalSort:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u: any, v: any):
        self.graph[u].append(v)

    def recursive_utils(self, vertex, visited, traverse):
        visited[vertex] = True

        for neighbour in self.graph[vertex]:
            if not visited[neighbour]:
                self.recursive_utils(neighbour, visited, traverse)

        traverse.append(vertex)

    def stack_traverse(self):
        visited = [False] * self.vertices
        top_order = []

        for i in range(self.vertices):
            if not visited[i]:
                self.recursive_utils(i, visited, top_order)

        return top_order[::-1]

    def traverse_in_degree(self):
        in_degree = [0] * self.vertices

        for vertex, neighbours in self.graph.items():
            for neighbour in neighbours:
                in_degree[neighbour] += 1

        queue = deque([])

        for idx in range(self.vertices):
            if in_degree[idx] == 0:
                queue.append(idx)

        count = 0
        top_order = []

        while queue:
            vertex = queue.popleft()

            top_order.append(vertex)

            for neighbour in self.graph[vertex]:
                in_degree[neighbour] -= 1

                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

            count += 1

        if count != self.vertices:
            print("Topological Sort has cycle.")
            return []

        return top_order


if __name__ == '__main__':
    g = TopologicalSort(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(1, 3)

    print("Following is a Topological Sort of the given graph")
    nodes = g.traverse_in_degree()
    print(nodes)

    print("Stack Traverse")
    nodes = g.stack_traverse()
    print(nodes)