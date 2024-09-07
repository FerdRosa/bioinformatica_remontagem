## Montagem de DNA a partir de k-mers: Um guia passo a passo com Grafos de De Bruijn

Este projeto utiliza o conceito de grafos de De Bruijn para remontar uma sequência de DNA a partir de seus k-mers (subsequências de tamanho k). O código fornecido implementa as etapas chave desse processo e gera um arquivo de saída com os resultados.

**O que é um Grafo de De Bruijn?**

Um grafo de De Bruijn é uma estrutura que representa as relações entre k-mers. Cada nó no grafo corresponde a um (k-1)-mer, e uma aresta direcionada conecta dois nós se seus (k-1)-mers se sobrepõem por k-2 caracteres e formam um k-mer.

**Por que usar Grafos de De Bruijn para Montagem de DNA?**

Grafos de De Bruijn são uma ferramenta poderosa para a montagem de DNA porque permitem reconstruir a sequência original a partir de fragmentos sobrepostos (k-mers). Encontrar um caminho Euleriano no grafo de De Bruijn equivale a encontrar a ordem correta dos k-mers que formam a sequência completa de DNA.

**Passo a passo do código**

1. **Leitura dos k-mers:** A função `read_kmers_from_file` lê os k-mers de um arquivo de entrada (composições.txt) e os armazena em uma lista.

2. **Construção do Grafo de De Bruijn:** A função `build_de_bruijn_graph` constrói o grafo de De Bruijn a partir dos k-mers. Cada k-mer é dividido em um prefixo (k-1)-mer e um sufixo (k-1)-mer, e uma aresta é adicionada ao grafo conectando o prefixo ao sufixo.

3. **Encontrando o Caminho Euleriano:** A função `find_eulerian_path` encontra um caminho Euleriano no grafo de De Bruijn. Um caminho Euleriano é um caminho que visita cada aresta do grafo exatamente uma vez. Esse caminho representa a ordem correta dos k-mers na sequência original de DNA.

4. **Reconstrução do DNA:** A função `reconstruct_from_path` reconstrói a sequência de DNA a partir do caminho Euleriano. O primeiro k-mer do caminho é usado como ponto de partida, e os k-mers subsequentes são adicionados, sobrepondo-se por k-1 caracteres.

5. **Escrita do Resultado:** A função `write_output_to_file` escreve o grafo de De Bruijn, o caminho Euleriano e a sequência de DNA reconstruída em um arquivo de saída (FernandoMartins.txt).

## Exemplo de Uso e Saída Esperada

**Entrada:**

Arquivo "compositions.txt" contendo os seguintes k-mers (com k=3):

```
TAA,AAT,ATG
```

**Saída:**

Arquivo "FernandoMartins.txt" contendo:

```
DNA Remontado:
TAATG
```

**Explicação:**

1. **Leitura dos k-mers:** O programa lê os k-mers `TAA`, `AAT` e `ATG` do arquivo "compositions.txt".

2. **Construção do Grafo de De Bruijn:** O grafo de De Bruijn é construído com os seguintes nós e arestas:

   * Nós: `TA`, `AA`, `AT`
   * Arestas: `TA` -> `AA`, `AA` -> `AT`, `AT` -> `TG`

3. **Encontrando o Caminho Euleriano:** O caminho Euleriano encontrado é `TA` -> `AA` -> `AT` -> `TG`.

4. **Reconstrução do DNA:** A partir do caminho Euleriano, a sequência de DNA original é reconstruída como `TAATG`.

5. **Escrita do Resultado:** O resultado "TAATG" é escrito no arquivo "FernandoMartins.txt".