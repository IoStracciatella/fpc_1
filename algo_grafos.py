import matplotlib.pyplot as plt
import numpy as np

class Grafo:
    
     # Inicializa o grafo com 'qtd_nos' nós
    def __init__(self, qtd_nos):
        self.qtd_nos = qtd_nos
        
        # Cria uma matriz de adjacência de tamanho qtd_nos x qtd_nos
        self.adj_matrix = [[0] * qtd_nos for _ in range(qtd_nos)]
        # Lista de coordenadas (x, y) para cada nó
        self.coordenadas = [(0, 0)] * qtd_nos

    def set_coord(self, no, x, y):
        # Define as coordenadas (x, y) para um nó
        if 0 <= no < self.qtd_nos:
            self.coordenadas[no] = (x, y)

    def add_aresta(self, no1, no2):
        # Adiciona uma aresta entre dois nós
        if 0 <= no1 < self.qtd_nos and 0 <= no2 < self.qtd_nos:
            self.adj_matrix[no1][no2] = 1
            self.adj_matrix[no2][no1] = 1

    def plot_grafo(self):
        # Função para plotar o grafo usando as coordenadas e a matriz de adjacência
        fig, ax = plt.subplots()
        
        # Desenha os nós
        for i, coord in enumerate(self.coordenadas):
            if coord is not None:  # Ignora nós deletados
                ax.plot(coord[0], coord[1], 'o', label=f'Nó {i}', markersize=10)
                ax.text(coord[0], coord[1], f'{i}', fontsize=12, ha='right')

        # Desenha as arestas
        for i in range(self.qtd_nos):
            for j in range(i + 1, self.qtd_nos):
                if self.adj_matrix[i][j] == 1 and self.coordenadas[i] is not None and self.coordenadas[j] is not None:
                    # Verifica se os nós estão ativos antes de desenhar a aresta
                    x_values = [self.coordenadas[i][0], self.coordenadas[j][0]]
                    y_values = [self.coordenadas[i][1], self.coordenadas[j][1]]
                    ax.plot(x_values, y_values, 'b-')  # linha azul para aresta

        ax.set_aspect('equal')
        plt.legend()
        plt.show()

# Função que cria uma árvore binária de 6 iterações (bifurcações)
def cria_rede_bifurcada():
    num_nos = 63  # 2^6 - 1 nós para uma árvore binária de 6 iterações
    grafo = Grafo(num_nos)

    # Colocando as coordenadas dos nós de forma que pareçam uma árvore bifurcada
    def coloca_nos(no, x, y, dx, depth):
        if no >= num_nos or depth > 5:
            return
        
        # Define a posição do nó atual
        grafo.set_coord(no, x, y)
        
        # Arestas com os nós filhos
        filho_esq = 2 * no + 1
        filho_dir = 2 * no + 2
        
        # Se os filhos existirem, adiciona as arestas
        if filho_esq < num_nos:
            grafo.add_aresta(no, filho_esq)
            coloca_nos(filho_esq, x - dx, y - 1, dx / 2, depth + 1)  # Coloca o filho esquerdo
            
        if filho_dir < num_nos:
            grafo.add_aresta(no, filho_dir)
            coloca_nos(filho_dir, x + dx, y - 1, dx / 2, depth + 1)  # Coloca o filho direito

    # Inicia a árvore a partir do nó 0
    coloca_nos(0, 0, 0, 10, 0)

    grafo.plot_grafo()

# Chama a função para criar e exibir a árvore
cria_rede_bifurcada()