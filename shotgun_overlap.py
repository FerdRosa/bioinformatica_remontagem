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
    suffix_counts = {}
    for node in graph:
        for neighbor in graph[node]:
            suffix_counts[neighbor] = suffix_counts.get(neighbor, 0) + 1

    start_node = None
    for node in graph:
        if node not in suffix_counts:
            start_node = node
            break

    print(f"\nComeçando com o nó inicial: {start_node}")
    path = [start_node]
    print(f"\nCaminho atual: {' -> '.join(path)}")

    while len(path) < len(graph):
        for neighbor in graph[path[-1]]:
            if neighbor not in path:
                path.append(neighbor)
                print(f"Adicionado ao caminho: {neighbor}")
                print(f"Caminho atual: {' -> '.join(path)}")
                break  # Sai do loop após adicionar o vizinho ao caminho
    return path


def StringComposition(Text, k):
    """
    Gera a composição k-mer de uma string Text.

    Args:
        Text: A string de DNA.
        k: O tamanho dos k-mers.

    Returns:
        Uma lista contendo todos os k-mers de Text em ordem lexicográfica.
    """

    kmers = []
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]  # Extrai o k-mer da posição atual
        kmers.append(kmer)  # Adiciona o k-mer à lista

    kmers.sort()  # Ordena os k-mers em ordem lexicográfica (dicionário)
    return kmers

Text = "ACGTTGCATGTCGCATGATG"
k = 4
composition = StringComposition(Text, k)
print(composition)

# Exemplo de uso
patterns = composition
overlap_graph = build_overlap_graph(patterns)

hamiltonian_path = find_hamiltonian_path(overlap_graph)
reconstructed_text = reconstruct_from_path(hamiltonian_path)

print("Grafo de Sobreposição:")
for node, neighbors in overlap_graph.items():
    if neighbors:
        print(f"{node} -> {' '.join(neighbors)}")

print("\nCaminho Hamiltoniano:", hamiltonian_path)
print("Texto Reconstruído:", reconstructed_text) 
