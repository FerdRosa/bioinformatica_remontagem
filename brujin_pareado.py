from collections import defaultdict, deque

# Função para construir o grafo de De Bruijn a partir de paired reads
def build_de_bruijn_graph(paired_reads, k, d):
    graph = defaultdict(list)
    for read in paired_reads:
        prefix = (read[0][:k-1], read[1][:k-1])
        suffix = (read[0][1:], read[1][1:])
        graph[prefix].append(suffix)
    return graph

# Função para encontrar um caminho Euleriano no grafo
def find_eulerian_path(graph):
    def find_start_node(graph):
        in_degree, out_degree = defaultdict(int), defaultdict(int)
        for node in graph:
            out_degree[node] += len(graph[node])
            for adj in graph[node]:
                in_degree[adj] += 1

        start, end = None, None
        for node in set(in_degree) | set(out_degree):
            if out_degree[node] > in_degree[node]:
                start = node
            if in_degree[node] > out_degree[node]:
                end = node

        return start or next(iter(graph))

    def dfs(node):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        path.appendleft(node)

    start_node = find_start_node(graph)
    path = deque()
    dfs(start_node)
    return list(path)

# Função para reconstruir a string a partir do caminho Euleriano
def reconstruct_string_from_pairs(path, k, d):
    prefix_string = path[0][0]
    suffix_string = path[0][1]
    
    for prefix, suffix in path[1:]:
        prefix_string += prefix[-1]
        suffix_string += suffix[-1]
    
    for i in range(k + d, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d]:
            return None  # no such string exists
    return prefix_string + suffix_string[-(k + d):]

# Função principal para reconstruir a string a partir de paired reads
def string_reconstruction_from_read_pairs(k, d, paired_reads):
    graph = build_de_bruijn_graph(paired_reads, k, d)
    print("Grafo de De Bruijn:")
    for node in graph:
        print(f"{node} -> {graph[node]}")
    
    path = find_eulerian_path(graph)
    print("\nCaminho Euleriano:")
    print(" -> ".join([str(p) for p in path]))
    
    reconstructed_string = reconstruct_string_from_pairs(path, k, d)
    return reconstructed_string

# Exemplo de entrada
k = 4
d = 2
paired_reads = [
    ("GAGA", "TTGA"),
    ("TCGT", "GATG"),
    ("CGTG", "ATGT"),
    ("TGGT", "TGAG"),
    ("GTGA", "TGTT"),
    ("GTGG", "GTGA"),
    ("TGAG", "GTTG"),
    ("GGTC", "GAGA"),
    ("GTCG", "AGAT")
]

# Reconstruir a string
result = string_reconstruction_from_read_pairs(k, d, paired_reads)
print("\nString Reconstruída:")
print(result)  # Saída esperada: GTGGTCGTGAGATGTTGA
