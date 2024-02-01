import heapq
from collections import defaultdict


class Dijkstra:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int, w: int):
        self.graph[u].append([v, w])

    def print_path(self, distances):
        print("Vertex Distance from Source")
        for i in range(self.vertices):
            print("{0}\t\t{1}".format(i, distances[i]))

    def calculate_path(self, start: int):
        distances = [float('inf')] * self.vertices

        distances[start] = 0
        hp = []
        heapq.heappush(hp, (0, start))

        while hp:
            distance, vertex = heapq.heappop(hp)

            for neighbour, cost in self.graph[vertex]:
                new_distance = cost + distance

                if distances[neighbour] > new_distance:
                    heapq.heappush(hp, (new_distance, neighbour))
                    distances[neighbour] = new_distance

        return distances


if __name__ == '__main__':
    graph = Dijkstra(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    distances = graph.calculate_path(0)
    graph.print_path(distances)