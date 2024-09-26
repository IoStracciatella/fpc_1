import matplotlib.pyplot as plt
import numpy as np

# Função fornecida inicialmente para o mapeamento logístico
def mapeamento_logistico_manual(a, N=5000, x0=0.1):
    # Lista para armazenar os valores de x
    x = [x0]
    
    # Itera N vezes para calcular a sequência
    for n in range(1, N):
        x_n = a * x[-1] * (1 - x[-1])
        x.append(x_n)
    
    # Calcula a média e variância
    media = sum(x) / N
    variancia = sum((xi - media) ** 2 for xi in x) / (N - 1)
    
    return x  # Retorna a lista de valores de x

# Função para gerar o diagrama de bifurcações
def diagrama_bifurcacoes(a_min, a_max, N=1000, x0=0.1, resolucao=1000, skip=100):
    # Gera os valores de 'a' com a resolução desejada
    a_values = np.linspace(a_min, a_max, resolucao)
    
    # Listas para armazenar os valores de 'a' e 'x_n'
    a_list = []
    x_list = []
    
    # Itera para cada valor de a
    for a in a_values:
        x = mapeamento_logistico_manual(a, N, x0)  # Usa a função já fornecida
        
        # Após as iterações iniciais, coleta os valores finais de x (comportamento assintótico)
        for xi in x[-skip:]:
            a_list.append(a)
            x_list.append(xi)
    
    # Plota o diagrama de bifurcações
    plt.figure(figsize=(10, 7))
    plt.plot(a_list, x_list, ',k', alpha=0.25)  # ',k' define pontinhos pretos
    plt.title('Diagrama de Bifurcações')
    plt.xlabel('Valor de a')
    plt.ylabel('Valores de x')
    plt.grid(True)
    plt.show()

# Chama a função para gerar o diagrama de bifurcações
diagrama_bifurcacoes(2.5, 4, N=1000, skip=100, resolucao=500)