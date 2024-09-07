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

# Exemplo de uso
Text = "ATCGAGCTAGGCTATCGATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"


k = 8
composition = StringComposition(Text, k)
print(composition)  # Saída: ['ATG', 'GGG', 'GGG', 'GGT', 'GTG', 'TAT', 'TGC', 'TGG']
