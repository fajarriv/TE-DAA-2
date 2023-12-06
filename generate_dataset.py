import os
import random


def generate_graph(num_of_vertex, max_edges):
    vertices = list(range(num_of_vertex))
    edges = set()

    while len(edges) < max_edges:
        v1 = random.choice(vertices)
        v2 = random.choice(vertices)

        # add edge if not self loop
        if v1 != v2:
            edge = (min(v1, v2), max(v1, v2))
            edges.add(edge)
    return vertices, list(edges)


def write_dataset(vertices, edges, filename):
    file_path = os.path.join('dataset', filename)
    with open(file_path, 'w') as file:
        # First line indicates number of vertices and edges
        file.write(f"{len(vertices)} {len(edges)}\n")
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]}\n")


def generate_dataset(num_of_vertex, max_edges, type):
    for i in range(1, 4):
        vertices, edges = generate_graph(num_of_vertex, max_edges)
        write_dataset(vertices, edges, f"dataset_{type}_{i}.txt")


def main():
    generate_dataset(16, 50, "kecil")
    generate_dataset(18, 75, "sedang")
    generate_dataset(20, 100, "besar")

if __name__ == "__main__":
    main()


print(generate_graph(5, 10))
