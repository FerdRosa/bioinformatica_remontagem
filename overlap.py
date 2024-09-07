def build_overlap_graph(patterns):
    """Constrói o grafo de sobreposição a partir de k-mers."""
    adj_list = {}
    for pattern in patterns:
        adj_list[pattern] = []
    for i in range(len(patterns)):
        suffix = patterns[i][1:]
        for j in range(len(patterns)):
            prefix = patterns[j][:-1]
            if suffix == prefix:
                adj_list[patterns[i]].append(patterns[j])
    return adj_list

def reconstruct_from_path(path):
    """Reconstrói a string original a partir de um caminho Hamiltoniano."""
    text = path[0]
    for i in range(1, len(path)):
        text += path[i][-1]
    return text

def find_hamiltonian_path(graph):
    """Encontra um caminho Hamiltoniano no grafo de sobreposição."""
    def visit(node, path, visited_edges):
        if len(path) == len(graph):
            return path
        for i, neighbor in enumerate(graph[node]):
            edge = (node, neighbor, i)
            if edge not in visited_edges:
                visited_edges.add(edge)
                path.append(neighbor)
                result = visit(neighbor, path, visited_edges)
                if result is not None:
                    return result
                path.pop()
                visited_edges.remove(edge)
        return None

    for start_node in graph:
        path = [start_node]
        visited_edges = set()
        result = visit(start_node, path, visited_edges)
        if result is not None:
            return result
    return None

# Exemplo de uso
patterns = ['ACGT', 'AGAG', 'AGCT', 'ATGA', 'ATGA', 'ATGC', 'ATGT', 'CATG', 'CATG', 'CATG', 'CGCA', 'CGTT', 'GAGA', 'GAGC', 'GATG', 'GCAT', 'GCAT', 'GCAT', 'GTCG', 'GTTG', 'TCGC', 'TGAG', 'TGAT', 'TGCA', 'TGCA', 'TGTC', 'TTGC']
overlap_graph = build_overlap_graph(patterns)

hamiltonian_path = find_hamiltonian_path(overlap_graph)
if hamiltonian_path:
    reconstructed_text = reconstruct_from_path(hamiltonian_path)
    print("Grafo de Sobreposição:")
    for node, neighbors in overlap_graph.items():
        if neighbors:
            print(f"{node} -> {' '.join(neighbors)}")

    print("\nCaminho Hamiltoniano:", hamiltonian_path)
    print("Texto Reconstruído:", reconstructed_text)
else:
    print("Não foi possível encontrar um caminho Hamiltoniano.")
