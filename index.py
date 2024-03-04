# Importando as bibliotecas necessárias
from collections import defaultdict, deque

# Definindo a classe Grafo
class Grafo:
    def __init__(self):
        # Inicializando o grafo como um defaultdict de listas
        self.grafo = defaultdict(list)

    def adicionar_aresta(self, origem, destino):
        # Adicionando uma aresta ao grafo, conectando a origem ao destino
        self.grafo[origem].append(destino)

    def busca_largura(self, inicio, objetivo):
        # Inicializando um conjunto de vértices visitados e uma fila de tuplas (vertice, caminho)
        visitados = set()
        fila = deque([(inicio, [inicio])])

        # Iniciando o loop principal da busca em largura
        while fila:
            # Desempilhando a fila para obter o vértice atual e o caminho até esse vértice
            vertice, caminho = fila.popleft()

            # Verificando se o vértice atual é o objetivo
            if vertice == objetivo:
                # Se sim, imprime o caminho encontrado
                print(f'Caminho de {inicio} até {objetivo}:', ' -> '.join(caminho))
                return

            # Se o vértice ainda não foi visitado
            if vertice not in visitados:
                # Adiciona o vértice aos visitados
                visitados.add(vertice)
                # Adiciona os vizinhos à fila, incluindo o caminho percorrido até o momento
                fila.extend((vizinho, caminho + [vizinho]) for vizinho in self.grafo[vertice])

        # Se o objetivo não foi alcançado, imprime que não há caminho
        print(f'Não há caminho de {inicio} até {objetivo}.')

# Criando o grafo e adicionando as arestas
grafo = Grafo()
arestas = [
    ('A', 'B'), ('A', 'E'), ('A', 'D'), ('B', 'C'), ('B', 'L'), ('E', 'F'), ('E', 'N'),
    ('D', 'I'), ('D', 'O'), ('C', 'S'), ('C', 'M'), ('F', 'G'), ('G', 'H'), ('I', 'J'),
    ('O', 'P'), ('J', 'K'), ('J', 'Q'), ('H', 'G'), ('G', 'F'), ('F', 'E'), ('N', 'E'),
    ('E', 'A'), ('S', 'C'), ('M', 'C'), ('C', 'B'), ('L', 'B'), ('B', 'A'), ('K', 'J'),
    ('Q', 'J'), ('J', 'I'), ('P', 'O'), ('I', 'D'), ('O', 'D'), ('D', 'A')
]

# Adicionando as arestas ao grafo
for aresta in arestas:
    grafo.adicionar_aresta(*aresta)

# Solicitando entrada e saída do usuário
entrada = input('Digite o vértice de entrada: ').upper()
saida = input('Digite o vértice de saída: ').upper()

# Realizando a busca em largura a partir do vértice de entrada até o vértice de saída
print(f"\nBusca em Largura de '{entrada}' até '{saida}':")
grafo.busca_largura(entrada, saida)
