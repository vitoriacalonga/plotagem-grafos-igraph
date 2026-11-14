import igraph

# 1. Instanciação do Grafo
# Inicializa a estrutura de dados do grafo vazia na memória
grafo = igraph.Graph()

# 2. Definição e adição dos vértices (nós)
# Substitua por categorias genéricas do seu projeto
nos = ["Nó A", "Nó B", "Nó C", "Nó D", "Nó E", "Nó F"]

# add_vertices cria os nós baseados em índices numéricos (0 a 5 neste caso)
grafo.add_vertices(len(nos))

# O prefixo .vs (vertex sequence) acessa as propriedades dos vértices. 
# Aqui injetamos os nomes da lista no atributo "name" de cada nó sequencialmente.
grafo.vs["name"] = nos

# 3. Definição das arestas (conexões) e pesos
# add_edges conecta os nós passando tuplas de (origem, destino) baseadas nos IDs numéricos
arestas = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4), (4, 5), (1, 5)]
grafo.add_edges(arestas)

# Pesos correspondentes a cada aresta (ex: distância, mobilidade, custo)
# A ordem reflete a ordem das conexões dos vértices em 'arestas'.
pesos = [15, 7, 22, 14, 30, 5, 12]

# O prefixo .es (edge sequence) acessa as propriedades das arestas.
# Criamos o atributo 'weight' e passamos a lista. 
grafo.es['weight'] = pesos

# 4. Customização visual (Cores Condicionais)
# Lógica em Python para colorir os nós. 
# Se o nó estiver na lista de destaque, fica verde claro, senão, branco.
nos_destaque = ["Nó A", "Nó C", "Nó F"]
cores = ["light green" if no in nos_destaque else "white" for no in nos]

# 5. Plotagem e exportação
# Chama o motor gráfico (Cairo) para renderizar a imagem com parâmetros de ajuste fino
igraph.plot(
    grafo, 
    "plot_exemplo.pdf",              # Nome e formato do arquivo de saída (.svg | .png |.pdf)
    bbox=(1000, 800),                # Resolução do arquivo gerado (largura x altura)
    margin=80,                       # Margem para evitar cortes nos nós da borda
    vertex_label=grafo.vs["name"],   # Usa o atributo "name" como texto dos nós
    vertex_color=cores,              # Aplica a lista de cores calculada acima
    vertex_label_color=(0, 0, 0),    # Cor do texto do nó em RGB 
    vertex_label_size=18,            # Tamanho da fonte do rótulo
    vertex_dist=80,                  # Aumenta o distanciamento físico entre os nós no desenho
    vertex_label_dist=1.5,           # Empurra o texto para fora da bolinha do nó
    edge_label=grafo.es['weight']    # Escreve o valor do peso no meio da linha da aresta
)