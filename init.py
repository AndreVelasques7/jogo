import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
width = 800
height = 600

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Criação da janela
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Meu Jogo")

# Carregamento e redimensionamento da imagem
image = pygame.image.load("imgs/marvin_2.png")
image = pygame.transform.scale(image, (100, 100))

# Posição inicial da imagem
image_x = width // 2 - 50
image_y = height // 2 - 50

pontuacao = 0


def atualizar_pontuacao():
    fonte = pygame.font.Font(None, 36)  # Escolha a fonte e o tamanho desejados
    texto_pontuacao = fonte.render("Pontuação: " + str(pontuacao), True, WHITE)
    window.blit(texto_pontuacao, (10, 10))  # Define a posição do texto na tela

def mover_imagem():
    # Define as novas coordenadas X e Y para a imagem
    new_x = random.randint(0, width - 100)
    new_y = random.randint(0, height - 100)

    # Atualiza as coordenadas da imagem
    global image_x, image_y
    image_x = new_x
    image_y = new_y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
           mouse_x, mouse_y = pygame.mouse.get_pos()
           if image_x <= mouse_x <= image_x + 100 and image_y <= mouse_y <= image_y + 100:
              # Aqui você pode adicionar o comportamento desejado ao clicar na imagem
              pontuacao += 1  # Incrementa a pontuação ao clicar na imagem
              mover_imagem()  # Move a imagem para uma nova posição

    # Preenchimento do fundo com a cor preta
    window.fill(BLACK)

    # Desenho da imagem
    window.blit(image, (image_x, image_y))

    # Atualização da pontuação
    atualizar_pontuacao()

    # Atualização da janela
    pygame.display.update()



