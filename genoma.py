from collections import defaultdict
from copy import deepcopy

def generate_composition(sequence, k):
    """Gera a composição k-mer de uma sequência em ordem alfabética."""
    print("Gerando composição k-mer...")
    return sorted([sequence[i:i+k] for i in range(len(sequence) - k + 1)])

def reconstruct_genome(composition):
    """Reconstrói um genoma a partir de uma lista de k-mers."""
    print("Reconstruindo genoma...")
    graph = defaultdict(list)
    for kmer in composition:
        prefix, suffix = kmer[:-1], kmer[1:]
        graph[prefix].append(suffix)

    print("Grafo antes de find_eulerian_cycle:", graph)  # Print adicionado

    contigs = []
    while graph:
        start = next(iter(graph))
        cycle = []
        find_eulerian_cycle(deepcopy(graph), cycle, start)
        contigs.append(cycle[0] + "".join(cycle[i][-1] for i in range(1, len(cycle))))

    return contigs

def find_eulerian_cycle(graph, cycle, start):
    """Encontra um ciclo Euleriano em um grafo."""
    stack = [start]
    while stack:
        current_node = stack[-1]
        if graph[current_node]:
            next_node = graph[current_node].pop()
            print(f"Encontrando ciclo Euleriano a partir de {current_node}...")
            stack.append(next_node)
        else:
            cycle.append(stack.pop())
    cycle.reverse()
    return cycle

def main():
    with open("input.txt", "r") as file:
        sequences = file.read().strip().split(",")

    k = int(input("Digite o valor de k: "))

    compositions = []
    genomes = []

    with open("composition.txt", "w") as comp_file:
        for i, sequence in enumerate(sequences, 1):  
            composition = generate_composition(sequence, k)
            compositions.append(f"{i}. {','.join(composition)}\n")
            genome = reconstruct_genome(composition)
            genomes.append(f"{i}. {genome}\n")

    with open("composition.txt", "w") as comp_file, open("output.txt", "w") as out_file:
        for line in compositions: 
            comp_file.write(line)

        for line in genomes:
            out_file.write(line)

if __name__ == "__main__":
    main()
