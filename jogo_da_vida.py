import pygame
import random

pygame.init()

#Definindo cores e propriedades do projeto
cor_preta = (255, 255, 255)
cor_cinza = (0, 0, 0)
cor_amarela = (255, 255, 255)

largura, altura = 800, 800
tamanho_quadrados = 10
largura_grade = largura // tamanho_quadrados
altura_grade = altura // tamanho_quadrados
FPS = 60

screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

# Gera números
def gen(num):
    return set([(random.randrange(0, altura_grade), random.randrange(0, largura_grade)) for _ in range(num)])

# Desenhando a grade de células
def desenhar_grade(posicao):
    for posicoes in posicao:
        colunas, linhas = posicoes
        parte_cima = (colunas * tamanho_quadrados, linhas * tamanho_quadrados)
        pygame.draw.rect(screen, cor_amarela, (*parte_cima, tamanho_quadrados, tamanho_quadrados))

    for linhas in range(altura_grade):
        pygame.draw.line(screen, cor_preta, (0, linhas * tamanho_quadrados), (largura, linhas * tamanho_quadrados))

    for colunas in range(largura_grade):
        pygame.draw.line(screen, cor_preta, (colunas * tamanho_quadrados, 0), (colunas * tamanho_quadrados, altura))

def ajustar_grade(positions):
    todos_vizinhos = set()
    new_positions = set()

    for position in positions:
        vizinhos = get_vizinhos(position)
        todos_vizinhos.update(vizinhos)

        vizinhos = list(filter(lambda x: x in positions, vizinhos))

        if len(vizinhos) in [2, 3]:
            new_positions.add(position)
    
    for position in todos_vizinhos:
        vizinhos = get_vizinhos(position)
        vizinhos = list(filter(lambda x: x in positions, vizinhos))

        if len(vizinhos) == 3:
            new_positions.add(position)
    
    return new_positions

def get_vizinhos(pos):
    x, y = pos
    vizinhos = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > largura_grade:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > altura_grade:
                continue
            if dx == 0 and dy == 0:
                continue

            vizinhos.append((x + dx, y + dy))
    
    return vizinhos

def main():
    rodando = True
    jogando = False
    contagem = 0
    freq_update = 120

    posicoes = set()
    while rodando:
        clock.tick(FPS)

        if jogando:
            contagem += 1
        
        if contagem >= freq_update:
            contagem = 0
            posicoes = ajustar_grade(posicoes)

        pygame.display.set_caption("Playing" if jogando else "Paused")

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // tamanho_quadrados
                row = y // tamanho_quadrados
                pos = (col, row)

                if pos in posicoes:
                    posicoes.remove(pos)
                else:
                    posicoes.add(pos)
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    jogando = not jogando
                
                if evento.key == pygame.K_c:
                    posicoes = set()
                    jogando = False
                    contagem = 0
                
                if evento.key == pygame.K_g:
                    posicoes = gen(random.randrange(4, 10) * largura_grade)
    
        screen.fill(cor_cinza)
        desenhar_grade(posicoes)
        pygame.display.update()


    pygame.quit()

# Impede que o código seja executado em outros projetos que importam o arquivo deste projeto
if __name__ == "__main__":
    main()