class HamiltonianBt():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.num_of_vertex = vertices
        self.is_hamiltonian_path = False

    def isSafe(self, current_v, pos, path):

        # Check if current vertex and last vertex in path are adjacent 
        if self.graph[path[pos-1]][current_v] == 0:
            return False

        for vertex in path:
            if vertex == current_v:
                return False

        return True

    def hamPathUtil(self, path, pos):
        # print(path)
        if pos == self.num_of_vertex:
            # self.printSolution(path)
            return True

        for v in range(1, self.num_of_vertex):
            if self.isSafe(v, pos, path) == True:
                path[pos] = v

                if self.hamPathUtil(path, pos+1) == True:
                    return True

                path[pos] = -1
        return False

    def hamPath(self):
        path = [-1] * self.num_of_vertex
        path[0] = 0

        if self.hamPathUtil(path, 1) == False:
            print("Solution does not exist\n")
            return False

        self.is_hamiltonian_path = True
        return True

    def printSolution(self, path):
        print("Solution Exists: Following",
              "is one Hamiltonian Path")
        for vertex in path:
            print(vertex, end=" ")
        print("\n")


g1 = HamiltonianBt(5)
g1.graph = [[0, 1, 0, 1, 0], 
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1,], 
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]

# Print the solution
g1.hamPath()

g2 = HamiltonianBt(5) 
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
        [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0], 
        [0, 1, 1, 0, 0], ] 

g2.hamPath(); 