from matplotlib import pyplot as plt

def mapeamento_logistico_manual(a, N=5000, x0=0.1):
    # Lista para armazenar os valores de x para plotagem
    x = [x0]
  
    # Gera a sequência, iterando N vezes para calcular os valores
    for n in range(1, N):
        x_n = a * x[-1] * (1 - x[-1])
        x.append(x_n)
    
    # Calcula a média e variância da sequência que foi gerada
    media = sum(x) / N
    variancia = sum((xi - media) ** 2 for xi in x) / (N - 1)
    
    return media, variancia

# Listas para armazenar os valores de a e das médias correspondentes
a_values = [1, 2, 3.8, 4]
medias = []

# Calcula a média para cada valor de a
for a in a_values:
    media, variancia = mapeamento_logistico_manual(a)
    medias.append(media)
    print(f'a={a}: média={media}, variância={variancia}')

# Plotando os valores de média em função de a
plt.plot(a_values, medias, 'o-', label='Média')
plt.xlabel('Valor de a')
plt.ylabel('Média')
plt.title('Média em função de a no Mapeamento Logístico')
plt.grid(True)
plt.legend()
plt.show()