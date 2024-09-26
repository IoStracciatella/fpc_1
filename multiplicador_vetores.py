# Importando as bibliotecas
import numpy as np
import time
from matplotlib import pyplot as plt

# Criando os vetores e uma função que atribui a eles valores aleatórios
def calcular_escalar(n):

    vetor_a = np.random.rand(n) 
    vetor_b = np.random.rand(n)  
    alfa = np.random.rand() 
    beta = np.random.rand()

    tempo_inicio = time.time()
    vetor_c = alfa * vetor_a + beta * vetor_b
    tempo_fim = time.time()
    tempo_exec = tempo_fim - tempo_inicio
    
    return vetor_c, tempo_exec

# Cria uma lista com cada dimensão utilizada e uma para os resultados a serem armazenados
dimensoes = [10**5, 10**6, 10**7, 10**8] 
resultados = []

# Aplica a função de calcular o vetor para cada valor em dimensoes
for n in dimensoes:
    c, tempo = calcular_escalar(n)
    resultados.append((n, c, tempo))
    print(f"Dimensão: {n}, Tempo de execução: {tempo:.6f} segundos")

# Armazena o tempo de execução
tempos_execucao = [resultado[2] for resultado in resultados]

# Funções do numpy para plotar o gráfico
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(dimensoes, tempos_execucao, marker='o')
plt.title('Tempo de Execução vs Dimensão (Escala Linear)')
plt.xlabel('Dimensão n')
plt.ylabel('Tempo de Execução (s)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.loglog(dimensoes, tempos_execucao, marker='o')
plt.title('Tempo de Execução vs Dimensão (Escala Log-Log)')
plt.xlabel('Dimensão n')
plt.ylabel('Tempo de Execução (s)')
plt.grid(True)

plt.tight_layout()
plt.show()