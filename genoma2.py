from collections import defaultdict

def generate_composition(sequence, k):
    """Gera a composição k-mer de uma sequência em ordem alfabética."""
    return sorted([sequence[i:i+k] for i in range(len(sequence) - k + 1)])

def reconstruct_genome(composition):
    """Reconstrói um genoma a partir de uma lista de k-mers."""
    graph = defaultdict(list)
    for kmer in composition:
        prefix, suffix = kmer[:-1], kmer[1:]
        graph[prefix].append(suffix)

    if not has_eulerian_path(graph):
        return None  # Não há caminho Euleriano

    cycle = []
    start_node = find_start_node(graph)
    find_eulerian_cycle(graph, cycle, start_node)

    genome = cycle[0]
    for i in range(1, len(cycle)):
        genome += cycle[i][-1]

    return genome

def has_eulerian_path(graph):
    """Verifica se o grafo tem um caminho Euleriano."""
    odd_degree_nodes = 0
    for node in graph:
        if len(graph[node]) % 2 == 1:
            odd_degree_nodes += 1
            if odd_degree_nodes > 2:
                return False
    return True

def find_eulerian_cycle(graph, cycle, start):
    """Encontra um ciclo ou caminho Euleriano em um grafo (iterativo)."""
    cycle.append(start)
    while graph:
        if start in graph:
            stack = [start]
            while stack:
                current_node = stack[-1]
                if graph[current_node]:
                    next_node = graph[current_node].pop()
                    stack.append(next_node)
                else:
                    cycle.append(stack.pop())
                    if not stack:
                        break
            start = cycle[-1]
        else:
            for i, node in enumerate(cycle):
                if node in graph:
                    cycle = cycle[i:] + cycle[:i]
                    start = node
                    break

    return cycle

def find_start_node(graph):
    """Encontra um nó inicial adequado para o caminho Euleriano."""
    for node in graph:
        if len(graph[node]) % 2 == 1:
            return node
    return next(iter(graph)) 

def main():
    with open("input.txt", "r") as file:
        sequences = file.read().strip().split(",")

    k = int(input("Digite o valor de k: "))

    with open("composition.txt", "w") as comp_file, open("output.txt", "w") as out_file:
        for i, sequence in enumerate(sequences, 1):
            composition = generate_composition(sequence, k)
            comp_file.write(f"Sequência {i}:\n")
            comp_file.write(",".join(composition) + "\n\n")

            genome = reconstruct_genome(composition)
            if genome:
                out_file.write(f"Sequência {i}:\n")
                out_file.write(genome + "\n\n")
            else:
                out_file.write(f"Sequência {i}: Genoma não reconstruído (grafo não Euleriano)\n\n")

if __name__ == "__main__":
    main()
