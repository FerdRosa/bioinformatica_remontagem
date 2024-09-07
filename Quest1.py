import time
from tqdm import tqdm

"""
    Entrada: sequência de caracteres e o tamanho K
    Saída : composição com o k-mers em ordem alfabética. Arquivo
    com linha única e k-mers separados por vírgula.
"""

def StringComposition(filename, k):
    with open(filename, 'r') as file:
        sequences = file.read().strip().split(',')

    with open("compositions.txt", 'w') as output_file:
        for seq_index, seq in enumerate(sequences, start=1):
            kmers = []
            for i in tqdm(range(len(seq) - k + 1), desc=f"Sequência {seq_index}", unit=" k-mer"):
                kmer = seq[i:i+k]
                kmers.append(kmer)
                time.sleep(0.000001)
            kmers.sort()

            output_file.write(",".join(kmers))

# Exemplo de uso
filename = "input.txt"
k = 50
StringComposition(filename, k)