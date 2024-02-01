import heapq
from collections import defaultdict


class PrimsAlgo:
    def __init__(self, vertices, graph):
        self.vertices = vertices
        self.graph = graph

    def generate_mst(self, start):
        edges = [(cost, start, to) for to, cost in self.graph[start].items()]

        heapq.heapify(edges)

        mst = defaultdict(set)

        visited = set()
        visited.add(start)

        total_cost = 0

        while edges:
            cost, frm, to = heapq.heappop(edges)

            if to not in visited:
                visited.add(to)
                mst[frm].add(to)

                total_cost += cost

                for to_next, next_cost in self.graph[to].items():
                    if to_next not in visited:
                        heapq.heappush(edges, (next_cost, to, to_next))

        return mst, total_cost


if __name__ == '__main__':
    example_graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
        'C': {'A': 3, 'B': 1, 'F': 5},
        'D': {'B': 1, 'E': 1},
        'E': {'B': 4, 'D': 1, 'F': 1},
        'F': {'C': 5, 'E': 1, 'G': 1},
        'G': {'F': 1},
    }

    g = PrimsAlgo(7, example_graph)
    edges, cost = g.generate_mst('A')
    print(dict(edges))
    print(cost)
