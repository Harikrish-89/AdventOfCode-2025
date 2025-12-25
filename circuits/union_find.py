from pprint import pprint


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, p):
        if p not in self.parent:
            self.parent[p] = p
            self.rank[p] = 1

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        # if root_p != root_q:
        #     self.parent[root_p] = root_q
        if root_p == root_q:
            return
        rank_p = self.rank[root_p]
        rank_q = self.rank[root_q]
        if rank_p < rank_q:
            self.parent[root_p] = root_q
        else:
            self.parent[root_q] = root_p
            if rank_p == rank_q:
                self.rank[root_p] += 1

    def show_all(self):
        pprint(self.parent)
