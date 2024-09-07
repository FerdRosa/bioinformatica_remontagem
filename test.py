from collections import defaultdict, deque

def build_de_bruijn_graph(kmers):
    """Constrói o grafo de De Bruijn a partir de k-mers."""
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph

def find_eulerian_path(graph):
    """Encontra um caminho Euleriano no grafo de De Bruijn."""
    def find_start_node():
        out_degrees = defaultdict(int)
        in_degrees = defaultdict(int)
        for node in graph:
            out_degrees[node] += len(graph[node])
            for neighbor in graph[node]:
                in_degrees[neighbor] += 1
        
        start = None
        for node in graph:
            if out_degrees[node] > in_degrees[node]:
                return node
        return next(iter(graph))
    
    def dfs(node):
        stack = [node]
        path = deque()
        while stack:
            current = stack[-1]
            if graph[current]:
                next_node = graph[current].pop()
                stack.append(next_node)
            else:
                path.appendleft(stack.pop())
        return list(path)
    
    start_node = find_start_node()
    return dfs(start_node)

def reconstruct_from_path(path):
    """Reconstrói a string original a partir de um caminho Euleriano."""
    text = path[0]
    for node in path[1:]:
        text += node[-1]
    return text

# Exemplo de uso
kmers = ['AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGCT', 'AGCTAGGC', 'AGGCTATC', 'ATCGAGCT', 'ATCGATGC', 'ATGCTAGC', 'CGAGCTAG', 'CGATGCTA', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGCTAG', 'CTAGGCTA', 'CTATCGAT', 'GAGCTAGG', 'GATGCTAG', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGCTA', 'GCTAGGCT', 'GCTATCGA', 'GGCTATCG', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGCTAGC', 'TAGGCTAT', 'TATCGATG', 'TCGAGCTA', 'TCGATGCT', 'TGCTAGCT']

de_bruijn_graph = build_de_bruijn_graph(kmers)
eulerian_path = find_eulerian_path(de_bruijn_graph)
reconstructed_text = reconstruct_from_path(eulerian_path)

print("Grafo de De Bruijn:")
for node, neighbors in de_bruijn_graph.items():
    if neighbors:
        print(f"{node} -> {' '.join(neighbors)}")

print("\nCaminho Euleriano:", eulerian_path)
print("Texto Reconstruído:", reconstructed_text)
