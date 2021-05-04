import pygame
import random

# CORES
fundo_verde = (114, 176, 29)
preto = (13, 10, 11)
vermelho = (193, 0 ,13)

# DIMENSÃO DA TELA
dimensoes = (600, 600)

# POSIÇÃO DA COBRINHA
x = 300
y = 300
d = 20

lista_cobra = [[x, y]]

delta_x = 0
delta_y = 0

x_comida = round(random.randrange(0, 600 - 2 * d) / 20) * 20
y_comida = round(random.randrange(0, 600 - 2 * d) / 20) * 20

pygame.init()
fonte = pygame.font.SysFont("hack", 35)

# TELA
tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Jogo da Cobrinha')
tela.fill(fundo_verde)

# CLOCK
clock = pygame.time.Clock()

# FUNÇÃO QUE DESENHA A COBRA


def desenha_cobra():
    tela.fill(fundo_verde)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, preto, [unidade[0], unidade[1], d, d])

# MOVE A COBRINHA


def mover_cobra(delta_x, delta_y, lista_cobra):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -d
                delta_y = 0

            elif event.key == pygame.K_RIGHT:
                delta_x = d
                delta_y = 0

            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -d

            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = d

    x_novo = lista_cobra[-1][0] + delta_x
    y_novo = lista_cobra[-1][1] + delta_y

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return delta_x, delta_y, lista_cobra


def verifica_comida(delta_x, delta_y, x_comida, y_comida, lista_cobra):
    head = lista_cobra[-1]
    x_novo = head[0] + delta_x
    y_novo = head[1] + delta_y

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
        x_comida = round(random.randrange(0, 600 - d) / 20) * 20
        y_comida = round(random.randrange(0, 600 - d) / 20) * 20

    pygame.draw.rect(tela, vermelho, [x_comida, y_comida, d, d])

    return x_comida, y_comida, lista_cobra


def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(601) or y not in range(601):
        raise Exception


def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()

    del corpo[-1]

    for x,y in corpo:
        if x == head[0] and y == head[-1]:
            raise Exception


def  atualizar_pontos(lista_cobra):
    pontos = str(len(lista_cobra))
    score = fonte.render("Pontuação: " + pontos, True, preto)
    tela.blit(score, [0, 0])


while True:
    pygame.display.update()

    desenha_cobra()
    delta_x, delta_y, lista_cobra = mover_cobra(delta_x, delta_y, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(delta_x, delta_y, x_comida, y_comida, lista_cobra)
    verifica_parede(lista_cobra)
    atualizar_pontos(lista_cobra)

    clock.tick(10)
