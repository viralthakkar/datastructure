from collections import defaultdict, deque


class ShortestPathUnweighted:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.nodes_matrix = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
        }

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def get_index(self, node):
        return self.nodes_matrix[node]

    def calculate_path(self, start):
        distance = [-1] * self.vertices
        distance[self.get_index(start)] = 0
        queue = deque([start])

        while queue:
            vertex = queue.popleft()

            for neighbour in self.graph[vertex]:
                if distance[self.get_index(neighbour)] == -1:
                    distance[self.get_index(neighbour)] = distance[self.get_index(vertex)] + 1
                    queue.append(neighbour)

        return distance


if __name__ == '__main__':
    s = ShortestPathUnweighted(7)
    s.add_edge('F', 'G')
    s.add_edge('C', 'F')
    s.add_edge('A', 'B')
    s.add_edge('A', 'D')
    s.add_edge('D', 'F')
    s.add_edge('C', 'A')
    s.add_edge('D', 'G')
    s.add_edge('E', 'G')
    s.add_edge('B', 'D')
    s.add_edge('B', 'E')
    s.add_edge('G', 'F')
    distance = s.calculate_path('C')
    print(distance)
