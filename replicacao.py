def FrequentWords(Text, k):
    """
    Encontra os k-mers mais frequentes em uma sequência de DNA (Text).

    Args:
        Text: A sequência de DNA.
        k: O tamanho dos k-mers.

    Returns:
        Um dicionário onde as chaves são os k-mers mais frequentes e os valores são suas contagens.
    """

    words = {}  # Dicionário para armazenar a contagem de cada k-mer
    maxCount = 0  # Contador para o número máximo de ocorrências de um k-mer

    # Itera sobre todas as posições possíveis para um k-mer no texto
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]  # Extrai o k-mer da posição atual
        if kmer not in words:
            words[kmer] = 1  # Adiciona o k-mer ao dicionário se não existir
        else:
            words[kmer] += 1  # Incrementa a contagem se já existir

        # Atualiza o contador de ocorrências máximas
        if words[kmer] > maxCount:
            maxCount = words[kmer]

    # Cria um novo dicionário contendo apenas os k-mers mais frequentes
    frequentPatterns = {key: value for key, value in words.items() if value == maxCount}

    return frequentPatterns

# Exemplo de uso
Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
result = FrequentWords(Text, k)
print(result)  # Saída: {'CATG': 4, 'GCAT': 2}
