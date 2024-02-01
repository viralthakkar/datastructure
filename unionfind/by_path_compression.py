class UnionFindByPath:
    def __init__(self, vertices):
        self.vertices = vertices
        self.nodes = [i for i in range(vertices)]
        self.rank = [0] * self.vertices

    def find_by_path_compression(self, x):
        if self.nodes[x] != x:
            self.nodes[x] = self.find_by_path_compression(self.nodes[x])

        return self.nodes[x]

    def find(self, x):
        if x == self.nodes[x]:
            self.nodes[x] = x
        return self.find(self.nodes[x])

    def union(self, u, v):
        u_p = self.find_by_path_compression(u)
        v_p = self.find_by_path_compression(v)

        if u_p == v_p:
            return True

        if self.rank[u_p] > self.rank[v_p]:
            self.nodes[v_p] = self.nodes[u_p]
        elif self.rank[u_p] < self.rank[v_p]:
            self.nodes[u_p] = self.nodes[v_p]
        else:
            self.nodes[u_p] = self.nodes[v_p]
            self.rank[v_p] += 1

        return False


if __name__ == '__main__':
    sf = UnionFindByPath(7)
    print(sf.nodes)
    sf.union(0, 1)
    a = sf.union(2, 1)
    print(a)
    b = sf.union(2, 0)
    print(b)
    sf.union(3, 0)
    sf.union(5, 2)
    sf.union(4, 3)
    sf.union(6, 5)
    print(sf.nodes)
    sf.union(5, 6)
    print(sf.nodes)
    sf.union(6, 5)
    print(sf.nodes)
    sf.union(0, 5)
    sf.union(6, 1)
    sf.union(1, 3)
    print(sf.nodes)

    print("Second Example")
    sf = UnionFindByPath(5)
    sf.union(0, 1)
    sf.union(1, 2)
    sf.union(2, 3)
    sf.union(3, 4)
    print(sf.nodes)