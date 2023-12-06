# This code adopted from
# https://www.geeksforgeeks.org/hamiltonian-path-using-dynamic-programming/
# contributed by maheshwaripiyush9

class HamiltonianDP:

    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
        self.num_of_vertex = vertices
        self.is_hamiltonian_path = False

    def Hamiltonian_path(self):
        
        dp = [[False for i in range(1 << self.num_of_vertex)] 
                    for j in range(self.num_of_vertex)]

        # Set all dp[i][(1 << i)] to
        # true
        for i in range(self.num_of_vertex):
            dp[i][1 << i] = True

        # Iterate over each subset
        # of nodes
        for i in range(1 << self.num_of_vertex):

            for j in range(self.num_of_vertex):

                # If the jth nodes is included
                # in the current subset
                if ((i & (1 << j)) != 0):

                    # Find K, neighbour of j
                    # also present in the
                    # current subset
                    for k in range(self.num_of_vertex):
                        if ((i & (1 << k)) != 0 and
                                self.graph[k][j] == 1 and
                                        j != k and
                            dp[k][i ^ (1 << j)]):
                            
                            # Update dp[j][i]
                            # to true
                            dp[j][i] = True
                            break
        
        # Traverse the vertices
        for i in range(self.num_of_vertex):

            # Hamiltonian Path exists
            if (dp[i][(1 << self.num_of_vertex) - 1]):
                self.is_hamiltonian_path = True
                return True

        # Otherwise, return false
        return False


# # Driver Code
# adj = [ [ 0, 1, 1, 1, 0 ] ,
#         [ 1, 0, 1, 0, 1 ],
#         [ 1, 1, 0, 1, 1 ],
#         [ 1, 0, 1, 0, 0 ] ]
 
# N = len(adj)

# graph = HamiltonianDP(N)
# graph.graph = adj
 
# if (graph.Hamiltonian_path()):
#     print("YES")
# else:
#     print("NO")