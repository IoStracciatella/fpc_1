import numpy as np
import matplotlib.pyplot as plt

# Função para lançar M dados N vezes
def lancar_dados(N, M):
    # Consideramos um dado de 6 lados, ou seja, os valores vão de 1 a 6
    dados = np.random.randint(1, 7, size=(N, M))
    # Soma dos valores dos M dados para cada uma das N tentativas
    soma_dados = np.sum(dados, axis=1)
    return soma_dados

# Função para plotar o histograma
def plot_histograma(N, M):
    # Realizar lançamentos e calcular as somas
    somas = lancar_dados(N, M)

    # Criar histograma com as somas
    counts, bins = np.histogram(somas, bins=range(M, 6*M + 2))

    # Plotar o histograma
    plt.stairs(counts, bins)
    plt.xlabel('Soma dos valores dos dados')
    plt.ylabel('Frequência')
    plt.title(f'Histograma para {N} lançamentos de {M} dados')
    plt.show()

# Menu para inserir o númeor de dados e lançamentos e replotar o histograma
while True:
    try:
        # Pede valores a pessoa
        N = int(input("Digite o número de lançamentos (N): "))
        M = int(input("Digite o número de dados (M): "))

        # Chama a função para plotar o histograma
        plot_histograma(N, M)
    except ValueError:
        print("Por favor, insira um número válido.") # Mesmo uma string sendo um valor numérico, eu resolvi não implementar pq não faz sentido
    
    # Perguntar se o usuário deseja continuar
    continuar = input("Deseja fazer outra simulação? (s/n): ").lower()
    if continuar != 's':
        break