from collections import defaultdict

def de_bruijn_graph(k, text):
    edges = []
    nodes = set()
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        prefix = kmer[:-1]
        suffix = kmer[1:]
        edges.append((prefix, suffix))
        nodes.add(prefix)
        nodes.add(suffix)
    
    graph = defaultdict(list)
    for prefix, suffix in edges:
        graph[prefix].append(suffix)
    
    return graph

def print_graph(graph):
    for node in graph:
        print(f"{node} -> {', '.join(graph[node])}")

def find_eulerian_path(graph):
    # Find all nodes with nonzero degree
    degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            degree[node] += 1
            degree[neighbor] -= 1

    # Find the start and end nodes
    start = end = None
    for node in degree:
        if degree[node] == 1:
            start = node
        elif degree[node] == -1:
            end = node

    # If there is an end node, add an edge from end to start
    if end is not None:
        graph[end].append(start)
    else:
        start = next(iter(graph))

    # Hierholzer's algorithm to find Eulerian path
    def find_cycle(start):
        stack = [start]
        path = []
        while stack:
            u = stack[-1]
            if graph[u]:
                v = graph[u].pop()
                stack.append(v)
            else:
                path.append(stack.pop())
        return path

    path = find_cycle(start)
    path = path[::-1]

    # Remove the added edge from end to start to get the correct path
    if end is not None:
        idx = path.index(end)
        if path[idx - 1] == start:
            path = path[idx:] + path[1:idx]

    return path

def reconstruct_genome(path):
    genome = path[0]
    for node in path[1:]:
        genome += node[-1]
    return genome

# Exemplo de uso
k = 5
text = "TAATGCCATGGGATGTT"
graph = de_bruijn_graph(k, text)
print("De Bruijn Graph:")
print_graph(graph)

path = find_eulerian_path(graph)

# Remover o último nó fictício se ele for igual ao primeiro nó
if path[0] == path[-1]:
    path = path[:-1]

print("\nEulerian Path:", " -> ".join(path))

genome = reconstruct_genome(path)
print("Reconstructed Genome:", genome)
