# Jogo da Vida de Conway

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensões da grade
largura, altura = 50, 50

# Configurações da simulação
print('-' * 30)
print('JOGO DA VIDA DE CONWAY!')
print('-' * 30)
frameRateJogo = int(input('Qual framerate você gostaria de utilizar? [PADRÃO: 200] n: '))

# Inicializa a grade com estados iniciais aleatórios
grade = np.random.choice([0, 1], size=(largura, altura))


# Função pra dar update na grade a cada geraçãp
def update(frameNum, img, grade, largura, altura):
    nova_grade = grade.copy()
    for x in range(largura):
        for y in range(altura):
            # Conta o N° de vizinhos vivos
            vizinhos = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                         (x, y - 1), (x, y + 1),
                         (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]

            vizinhos_vivos = sum(grade[i % largura, j % altura] for i, j in vizinhos)

            # Aplica as regras do jogo da vida
            if grade[x, y] == 1:
                if vizinhos_vivos < 2 or vizinhos_vivos > 3:
                    nova_grade[x, y] = 0
            else:
                if vizinhos_vivos == 3:
                    nova_grade[x, y] = 1

    img.set_data(nova_grade)
    grade[:] = nova_grade[:]
    return img


# Cria uma figura e eixos para a visualização
figura, eixo = plt.subplots()
img = eixo.imshow(grade, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(figura, update, fargs=(img, grade, largura, altura), frames=10, interval=frameRateJogo)

plt.title('Jogo da Vida de Conway | FPS: {}'.format(frameRateJogo))
plt.show()
