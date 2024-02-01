from unionfind.by_path_compression import UnionFindByPath


class KruskalAlgo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def generate_mst(self):
        edges = sorted(self.graph, key=lambda x: x[2])
        uf = UnionFindByPath(self.vertices)

        i = e = 0

        result = []

        while e < self.vertices - 1:
            u, v, w = edges[i]
            i += 1

            if not uf.union(u, v):
                e += 1
                result.append([u, v, w])

        return result, sum(map(lambda x: x[2], result))


if __name__ == '__main__':
    g = KruskalAlgo(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 0, 4)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 2, 3)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 2, 4)
    g.add_edge(4, 3, 3)
    g.add_edge(5, 2, 2)
    g.add_edge(5, 4, 3)
    res, cost = g.generate_mst()
    print(res, cost)
