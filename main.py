import os
import time
import tracemalloc

from hamiltonian_backtracking import HamiltonianBt
from hamiltonian_dp import HamiltonianDP


def make_graph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_of_vertex, num_of_edges = map(int, lines[0].split())
        adj_matrix = [[0 for i in range(num_of_vertex)]
                      for j in range(num_of_vertex)]
        for line in lines[1:]:
            
            v1, v2 = map(int, line.split())
            adj_matrix[v1][v2] = 1
            adj_matrix[v2][v1] = 1
        return num_of_vertex, adj_matrix


def measure_dp(file_path):
    num_of_vertex, adj_matrix = make_graph(file_path)
    graph = HamiltonianDP(num_of_vertex)
    graph.graph = adj_matrix

    tracemalloc.start()
    start = time.perf_counter()

    graph.Hamiltonian_path()

    time_taken = (time.perf_counter() - start) * 1000 # in ms
    memory_peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    tracemalloc.clear_traces()
    result = graph.is_hamiltonian_path

    return result, time_taken, memory_peak

def measure_backtracking(file_path):
    num_of_vertex, adj_matrix = make_graph(file_path)
    graph = HamiltonianBt(num_of_vertex)
    graph.graph = adj_matrix

    tracemalloc.start()
    start = time.perf_counter()

    graph.hamPath()

    time_taken = (time.perf_counter() - start) * 1000 # in ms
    memory_peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    tracemalloc.clear_traces()
    result = graph.is_hamiltonian_path

    return result, time_taken, memory_peak

def compare_algorithm(file):
    folder = 'dataset'
    pathname = os.path.join(folder, file)
    
    dp_result, dp_time, dp_memory = measure_dp(pathname)
    bt_result, bt_time, bt_memory = measure_backtracking(pathname)

    print(f"\n Dataset: {file}")
    print(f"DP: {dp_result} {dp_time}ms {dp_memory}B")
    print(f"Backtracking: {bt_result} {bt_time}ms {bt_memory}B")




def main():
    allFiles = [
        'dataset_kecil_1.txt', 'dataset_kecil_2.txt', 'dataset_kecil_3.txt',
        'dataset_sedang_1.txt', 'dataset_sedang_2.txt', 'dataset_sedang_3.txt',
        'dataset_besar_1.txt', 'dataset_besar_2.txt', 'dataset_besar_3.txt',
    ]
    for file in allFiles:
        compare_algorithm(file)
        print("====================================")


if __name__ == "__main__":
    main()
