# Plotagem de Redes Complexas e Grafos Ponderados 

Este repositório contém uma estrutura base didática para a modelagem, estilização e plotagem de redes complexas utilizando a biblioteca `igraph` em Python. 

O script oferece um modelo seguro e generalizado para a visualização de grafos ponderados, permitindo a customização de vértices, arestas, pesos e cores condicionais, exportando o resultado final em formatos de alta qualidade gráfica (SVG ou PNG).

## Pré-requisitos e Instalação

A plotagem no `igraph` requer o motor gráfico Cairo. Para evitar conflitos de ambiente (como o erro `PEP 668` restrito pelo sistema no Linux) e falhas de dependência visual (`AttributeError: Plotting not available`), é fundamental utilizar um ambiente virtual.

Siga as instruções correspondentes ao seu sistema operacional:

### No Windows
1. Abra o terminal na pasta do projeto, crie e ative o ambiente virtual:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```
2. Instale o pacote principal e o `pycairo` (que já inclui os binários pré-compilados para Windows):
   ```cmd
   pip install igraph pycairo
   ```

### No Linux (Ubuntu/Debian)
1. Abra o terminal, crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instale o pacote principal e o `cairocffi` (ponte gráfica nativa para o ecossistema Linux):
   ```bash
   pip install igraph cairocffi
   ```

## 🚀 Como Executar

Com o ambiente ativado, execute o script base de plotagem:

```bash
python plot_template.py
```
A imagem do grafo será renderizada e salva automaticamente no diretório atual.

## 🧠 Estrutura de Modelagem

Para adaptar este modelo aos seus próprios dados de pesquisa, estes são os conceitos-chave estruturados no script:

* **`igraph.Graph()`**: Inicializa a estrutura de dados na memória.
* **`grafo.add_vertices(N)`**: Cria os vértices indexados numericamente (0 a N).
* **`grafo.add_edges([...])`**: Mapeia as conexões utilizando tuplas de IDs numéricos `(origem, destino)`.
* **Atributos `.vs` e `.es`**:
  * `grafo.vs["name"]`: Armazena os rótulos visuais dos vértices (Vertex Sequence).
  * `grafo.es['weight']`: Atribui a lista de pesos estruturais nas arestas (Edge Sequence).
* **`igraph.plot(...)`**: Função de renderização em Cairo. Permite ajustes finos como resolução (`bbox`), margens seguras (`margin`), espaçamento físico para grafos densos (`vertex_dist`) e aplicação de regras de cores nos nós.