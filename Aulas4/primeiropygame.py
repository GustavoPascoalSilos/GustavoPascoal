import pygame

#Inicializar o pygame
pygame.init()

tamanho = (900, 500)

#Cria uma tela com tamanho especificado
tela = pygame.display.set_mode(tamanho)

#Define o titulo da janela
pygame.display.set_caption("Hello Games!")

#Define um relógio para controlar o FPS
relogio = pygame.time.Clock()

posicaoBola = pygame.Vector2(450, 250)
direcaoY = 1
direcaoX = 1
velBola = 200
dt = 0

while True:
    #Lida com os eventos da aplicação
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit() #Fechando o pygame

    #Preenche a tela com uma cor
    tela.fill((24, 190, 157))
    
    #Desenha um circulo na tela
    pygame.draw.circle(tela, (0,0,0), posicaoBola, 50)

    posicaoBola.y += velBola * direcaoY * dt
    if posicaoBola.y >= 450:
        direcaoY = -1
    elif posicaoBola.y <= 50:
        direcaoY = 1

    posicaoBola.x += velBola * direcaoX * dt
    if posicaoBola.x >= 850:
        direcaoX = -1
    elif posicaoBola.x <= 50:
        direcaoX = 1

    

    #Atualiza a tela
    pygame.display.update()
    #Define a quantidade de FPS
    dt = relogio.tick(60)/ 1000