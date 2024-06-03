from sys import *


class Graph:
    def __init__(self):
        self.V = int(input())
        self.g = [list(map(int, input().split())) for _ in range(self.V)]

    def find_min_idx(self, k, mst_set):
        min = 10**7
        for v in range(self.V):
            if k[v] < min and not mst_set[v]:
                min = k[v]
                idx = v
        return idx

    def prim_MST(self):
        k = [0] + [10**7] * (self.V-1)
        mst = [-1] * self.V
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.find_min_idx(k, mst_set)
            mst_set[u] = True
            for v in range(self.V):
                if self.g[u][v] > 0 and not mst_set[v] and k[v] > self.g[u][v]:
                    k[v] = self.g[u][v]
                    mst[v] = u

        for i in range(1, self.V):
            print(mst[i]+1, i+1)


def main():
    Graph().prim_MST()


if __name__ == '__main__':
    main()
