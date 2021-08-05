from parser import Parser
import math
import random


class Solver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.print()
    def not_solved(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.matrix[i][j] == 0:
                    return True
        return False

    def get_high_low(self, idx):
        if idx < 3:
            return (0, 3)
        elif idx < 6:
            return (3, 6)
        else:
            return (6, 9)

    def get_row(self, idx):
        for i in self.matrix[idx]:
            if i != 0:
                yield i

    def get_column(self, idx):
        for i in range(9):
            if self.matrix[i][idx] != 0:
                yield self.matrix[i][idx]

    def get_grid(self, i, j):

        lowi, highi = self.get_high_low(i)
        lowj, highj = self.get_high_low(j)

        for i in range(lowi, highi):
            for j in range(lowj, highj):
                if self.matrix[i][j] != 0:
                    yield self.matrix[i][j]

    def explore_missing(self, i, j):
        seen = set()
        unseen = set([i for i in range(1, 10)])
        for elem in self.get_row(i):
            seen.add(elem)
        for elem in self.get_column(j):
            seen.add(elem)
        for elem in self.get_grid(i, j):
            seen.add(elem)
        return unseen.difference(seen)

    def print(self):
        print("-"*20)
        print(*self.matrix, sep="\n")
        print("-"*20)

    def solve(self):
        while self.not_solved():
            for i in range(0, 9):
                for j in range(0, 9):
                    #print(f"missing {self.explore_missing(i, j)} in {i}{j}")
                    if self.matrix[i][j] != 0:
                        continue
                    missing = self.explore_missing(i, j)
                    if len(missing) == 1:
                        self.matrix[i][j] = missing.pop()


if __name__ == "__main__":
    data = Parser("datasets/sudoku.csv")
    data.read_data()
    n = len(data.questions)
    idx = random.randint(0, n)
    print(f"solving sudoku number {idx}")
    sample = data.questions[idx]
    solver = Solver(sample)
    solver.solve()
    solver.print()
#solver.explore_missing()
