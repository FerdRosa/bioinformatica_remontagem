from collections import defaultdict, deque
import time
from tqdm import tqdm

"""
    Crie um programa chamado assembler capaz de remontar uma sequência genética a
    partir de um arquivo texto contendo os kmers em ordem lexicográfica.
    O programa deverá montar a sequência e gerar um arquivo TXT com a sequência de
    DNA REMONTADA.
    ARQUIVO DE SAÍDA: Arquivo texto com uma única linha contendo o DNA remontado e
    nomeado com seu primeiro e último nome. Extensão TXT. 
"""



def read_file(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        kmers = line.split(',')
    return kmers

def bruijn_graph(kmers):
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
        # print(f"Adicionando aresta: {prefix} -> {suffix}")
    return graph

def eulerian_path(graph):
    def find_start_node():
        saida = defaultdict(int)
        entrada = defaultdict(int)
        for node in graph:
            saida[node] += len(graph[node])
            for neighbor in graph[node]:
                entrada[neighbor] += 1
        
        for node in graph:
            if saida[node] > entrada[node]:
                # print(f"Nó inicial encontrado: {node}")
                return node
        # print("Nó inicial não encontrado, usando o primeiro nó do grafo.")
        return next(iter(graph))
    
    def dfs(node):
        stack = [node]
        path = deque()
        while stack:
            current = stack[-1]
            if graph[current]:
                next_node = graph[current].pop()
                # print(f"Explorando aresta: {current} -> {next_node}")
                stack.append(next_node)
            else:
                path.appendleft(stack.pop())
        return list(path)
    
    start_node = find_start_node()
    return dfs(start_node)

def reconstruct_from_path(path):
    text = path[0]
    for node in path[1:]:
        text += node[-1]
    return text

def write_oufile(filename, reconstructed_text):
    with open(filename, 'w') as file:
        
        file.write(reconstructed_text)


input_filename = 'compositions.txt'
output_filename = 'FernandoMartins.txt'

print("Lendo k-mers do arquivo...")
kmers = read_file(input_filename)
print("K-mers lidos com sucesso.")

print("Construindo o grafo de De Bruijn...")
for _ in tqdm(range(100), desc="Progresso da construção do grafo"):
    time.sleep(0.002)  
de_bruijn_graph = bruijn_graph(kmers)
print("Grafo de De Bruijn construído com sucesso.")

print("Encontrando o caminho Euleriano...")
for _ in tqdm(range(100), desc="Progresso da busca pelo caminho Euleriano"):
    time.sleep(0.002)  
eulerian_path = eulerian_path(de_bruijn_graph)
print("Caminho Euleriano encontrado com sucesso.")

print("Reconstruindo o DNA...")
for _ in tqdm(range(100), desc="Progresso da reconstrução do DNA"):
    time.sleep(0.002)  
reconstructed_text = reconstruct_from_path(eulerian_path)
print("DNA reconstruído com sucesso.")

print("Escrevendo o resultado no arquivo de saída...")
write_oufile(output_filename, reconstructed_text)
print(f"Resultado escrito com sucesso no arquivo {output_filename}.")
