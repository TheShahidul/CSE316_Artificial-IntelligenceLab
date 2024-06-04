import random

class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]             #shahidul
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.goal_level = 9999999
        self.state = 0

    def generate_grid(self):
        self.N = int(input("Matrix size: "))
        graph = [[random.choice([0, 1]) for i in range(self.N)] for j in range(self.N)]
        return graph
    
    def init(self):
        graph = self.generate_grid()

        start_x = int(input("Enter the x coordinate of the source: "))
        start_y = int(input("Enter the y coordinate of the source: "))
        goal_x = int(input("Enter the x coordinate of the goal: "))
        goal_y = int(input("Enter the y coordinate of the goal: "))

        self.source = Node(start_x, start_y, 0)
        self.goal = Node(goal_x, goal_y, self.goal_level)

        print("matrix:")

        for row in graph:
            print(row)

        self.st_dfs(graph, self.source)

        if self.found:
            print("Path found")
            print("Path length: ", self.goal_level)
        else:
            print("Path not found")

    def print_direction(self, m, x, y):
        if m == 0:
            print("Move down ({},{})".format(x, y))
        elif m == 1:
            print("Move up ({},{})".format(x, y))
        elif m == 2:
            print("Move right ({},{})".format(x, y))
        elif m == 3:
            print("Move left ({},{})".format(x, y))

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            if (0 <= v_x < self.N) and (0 <= v_y < self.N) and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1
                self.print_direction(j, v_x, v_y)
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal_level = v_depth
                    return
                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)
                if self.found:
                    return

def main():
    dfs = DFS()
    dfs.init()

if __name__ == "__main__":
    main()
