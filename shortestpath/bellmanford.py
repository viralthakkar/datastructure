class BellManFord:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u: int, v: int, w: any):
        self.graph.append([u, v, w])

    def calculate_path(self, start: int):
        distances = [float("inf")] * self.vertices

        distances[start] = 0

        for _ in range(self.vertices - 1):
            for u, v, w in self.graph:
                if distances[u] != float("inf") and distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w

        for u, v, w in self.graph:
            if distances[u] != float("inf") and distances[v] > distances[u] + w:
                print("Graph Contains Cycle")
                break

        return distances


if __name__ == '__main__':
    g = BellManFord(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    # add below one to check the cycle
    # g.add_edge(3, 3, -3)

    res = g.calculate_path(0)
    print(res)