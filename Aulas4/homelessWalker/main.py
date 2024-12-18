import pygame
from random import randint

pygame.init()
relogio = pygame.time.Clock()

tamanhoTela = (1280, 720)
tela = pygame.display.set_mode(tamanhoTela)

pygame.display.set_caption("Homeless Walker")
dt = 0

# Carrega a fonte a ser usada no jogo
fonteTempo = pygame.font.Font("assets/Fonts/Energy Station.ttf", 80)

# Carrega a spritesheet para nosso projeto
folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle_2.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()
folhaSpritesJump = pygame.image.load("assets/Homeless_1/Jump.png").convert_alpha()
folhaSpritesRunn = pygame.image.load("assets/Homeless_1/Run.png").convert_alpha()
folhaSpritesDead = pygame.image.load("assets/Homeless_1/Dead.png").convert_alpha()

# Define os frames
listFramesIdle = []
listFramesWalk = []
listFramesJump = []
listFramesRunn = []
listFramesDead = []

#Lista para guardar os obstaculos
listaObstaculos = []

# Cria os frames do personagem na lista de listFramesIdle
for i in range(11):
    # Pega um frame da folha de sprites na posição i * 0, 0 com tamanho 128x128
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    # Redimensiona o frame para 2 vezes o tamanho original
    frame = pygame.transform.scale2x(frame)
    # Adiciona o frame na lista de listFramesIdle
    listFramesIdle.append(frame)

for i in range(8):
    frame = folhaSpritesWalk.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesWalk.append(frame)

for i in range(9):
    frame = folhaSpritesJump.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesJump.append(frame)

for i in range(8):
    frame = folhaSpritesRunn.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesRunn.append(frame)

for i in range(4):
    frame = folhaSpritesDead.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    listFramesDead.append(frame)


# Variaveis da animação do personagem parado
indexFrameIdle = 0 # Controla qual imagem está sendo mostrada na tela
tempoAnimacaoIdle = 0.0 # Controla quanto tempo se passou desde a última troca de frame
velocidadeAnimacaoIdle = 5 # Controlar o tempo de animação em relação ao tempo real (1 / velocidadeAnimacaoIdle)

# Variaveis da animação do personagem andando
indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

# Variaveis da animação do personagem pulando
indexFrameJump = 0
tempoAnimacaoJump = 0.0
velocidadeAnimacaoJump = 5

# Variaveis da animação do personagem correndo
indexFrameRunn = 0
tempoAnimacaoRunn = 0.0
velocidadeAnimacaoRunn = 10

#Variaveis da animação do personagem morto
indexFrameDead = 0
tempoAnimacaoDead = 0.0
velocidadeAnimacaoDead = 2

# Retangulo do personagem na tela para melhor controle e posicionamento do personagem
personagemRect = listFramesIdle[0].get_rect(midbottom=(250, 480))
personagemColisaoRect = pygame.Rect(personagemRect.x, personagemRect.x, 80, 120)

gravidade = 1 # Gravidade do jogo, valor que aumenta a cada frame
direcaoPersonagem = 1 # Direção que o personagem está olhando (1 = Direita, -1 = Esquerda)
estaAndando = False # Define se o personagem está andando ou não


velocidadeArmas = 20

#ASSETS PARA AS ARMAS
#Importa as imagens das armas
listaImagemObstaculo = [
    pygame.image.load(f"assets/Weapons/Icons/Icon28_{i:02d}.png").convert_alpha() for i in range (1, 40)

]

for i in range(len(listaImagemObstaculo)):
    #Redimencionar a imagem
    listaImagemObstaculo[i] = pygame.transform.scale(listaImagemObstaculo[i], (50, 50))
    #Inverter a imagem
    listaImagemObstaculo[i] = pygame.transform.flip(listaImagemObstaculo[i], True, False)
    #Rotacionar a imagem
    listaImagemObstaculo[i] = pygame.transform.rotate(listaImagemObstaculo[i], 35)


# ICONES
iconeVida = pygame.image.load("assets/Icons/Icon12.png").convert_alpha()
iconeVida = pygame.transform.scale2x(iconeVida)


# ASSETS PARA O PLANO DE FUNDO
# Importa as imagens do plano de fundo
listBgImages = [
    pygame.image.load("assets/Apocalipse/Apocalypse3/Pale/sky.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypse3/Pale/moon.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypse3/Pale/sand_back.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypse3/Pale/sand&objects3.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypse3/Pale/sand&objects2.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypse3/Pale/sand&objects1.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Apocalypse3/Pale/sand.png").convert_alpha(),  
]

listaBgVelocidades = [1, 3, 7, 9, 10, 15, 20] # Velocidades de cada imagem do plano de fundo

listaBgPosicoes = [0 for _ in range(len(listBgImages))] # Posições de cada imagem do plano de fundo

# Loop que redimensiona as imagens do plano de fundo
for i in range(len(listBgImages)):
    listBgImages[i] = pygame.transform.scale(listBgImages[i], tamanhoTela)

ALTURA_CHAO = 485
velocidadePersonagem = 30
vidas = 3
GameOver = False
tempoJogo = 0


# Evento para aumentar a dificuldade do jogo
AUMENTA_DIFICULDADE = pygame.USEREVENT + 1 
# Aumenta a dificuldade a cada 10 segundos
pygame.time.set_timer(AUMENTA_DIFICULDADE, 10000) 

tempoMaximoaEntreObstaculos = 3000
#Evento para adicionar os obstaculos
ADICIONA_OBSTACULO = pygame.USEREVENT + 2
#Define um timer para adicionar os obstaculos
pygame.time.set_timer(ADICIONA_OBSTACULO, randint(500, tempoMaximoaEntreObstaculos))

# LOOP PRINCIPAL
while True:
    # Loop que verifica todos os eventos que acontecem no jogo
    for event in pygame.event.get():

        # Verifica se o evento é de fechar a janela
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha o jogo
            exit() # Fecha o programa
        
        if not GameOver:
            if event.type == AUMENTA_DIFICULDADE:
                velocidadePersonagem += 4
                
                if tempoMaximoaEntreObstaculos > 1100:
                    tempoMaximoaEntreObstaculos -= 300
                    pygame.time.set_timer(ADICIONA_OBSTACULO, randint(800, tempoMaximoaEntreObstaculos))
            
            if event.type == ADICIONA_OBSTACULO:
                obstaculoImage = listaImagemObstaculo[randint(0, len(listaImagemObstaculo) - 1)] 
                posicaoX = randint(1280, 1500)
                obstaculoRect = obstaculoImage.get_rect(midbottom=(posicaoX, 620))
                
                obstaculo = {
                    "rect": obstaculoRect,
                    "image": obstaculoImage
                }

                listaObstaculos.append(obstaculo)

                

    #tela.fill((255, 255, 255)) # Preenche a tela com a cor branca

    if vidas <= 0:
        GameOver = True

    # Percorre todas as imagens do plano de fundo para movimentar
    for i in range(len(listBgImages)):
        if estaAndando:
            listaBgPosicoes[i] -= listaBgVelocidades[i] * velocidadePersonagem * dt * direcaoPersonagem # Move a imagem para a esquerda

        # Verifica se a imagem saiu da tela para a esquerda
        if listaBgPosicoes[i] <= -tamanhoTela[0]:
            listaBgPosicoes[i] = 0 # Retorna a imagem para a posição inicial

        # Verifica se a imagem saiu da tela para a direita
        if listaBgPosicoes[i] >= tamanhoTela[0]:
            listaBgPosicoes[i] = 0

    # Desenha o plano de fundo
    for i in range(len(listBgImages)):
        # Desenha a imagem do plano de fundo que está na tela
        tela.blit(listBgImages[i], (listaBgPosicoes[i], 0))

        # Desenha a imagem do plano de fundo que está fora da tela na direita
        tela.blit(listBgImages[i], (listaBgPosicoes[i] + tamanhoTela[0], 0))

        # Desenha a imagem do plano de fundo que está fora da tela na esquerda
        tela.blit(listBgImages[i], (listaBgPosicoes[i] + -tamanhoTela[0], 0))

    
    for obstaculo in listaObstaculos:
        obstaculo["rect"].x -= 30 * velocidadePersonagem * dt
        # Verifica se o obstáculo saiu da tela
        if obstaculo["rect"].x < 0:
            listaObstaculos.remove(obstaculo)
            
        tela.blit(obstaculo["image"], obstaculo["rect"])

        # Verifica se houve colisão entre o personagem e o obstáculo
        if personagemColisaoRect.colliderect(obstaculo["rect"]):
            listaObstaculos.remove(obstaculo)
            vidas -= 1

    
    # Atualiza o tempo de jogo
    if not GameOver:
        tempoJogo += dt


    # Cria o texto para o tempo de jogo
    textoTempo = fonteTempo.render(str(int(tempoJogo)), False, (255, 255, 255))

    # Desenha o tempo de jogo na tela
    tela.blit(textoTempo, (tamanhoTela[0] / 2, 30))


    #Desenha o texto para vidas
    for i in range(vidas):
        tela.blit(iconeVida, (20 + i * iconeVida.get_width(), 20))


    if GameOver:
        # Cria o texto para o menu de reiniciar o jogo
        textoGameOver = fonteTempo.render("JAH ERA!", False, (255, 255, 255))
        textoReiniciar = fonteTempo.render("APERTE ENTER PARA REINICIAR", False, (255, 255, 255))
        # Desenha o menu de reiniciar o jogo na tela
        tela.blit(textoGameOver, (484, 260))
        tela.blit(textoReiniciar, (84, 360))


    # Soma o tempo que se passou desde o último frame
    tempoAnimacaoIdle += dt

    # Verifica se o tempo de animação do personagem parado é maior ou igual ao tempo de animação
    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        # Atualiza o frame do personagem parado de acordo com a lista de frames
        indexFrameIdle = (indexFrameIdle + 1) % len(listFramesIdle)
        tempoAnimacaoIdle = 0.0 # Reseta o tempo entre os frames

    # Atualiza a animação do personagem andando
    tempoAnimacaoWalk += dt
    
    # Verifica se o tempo de animação do personagem andando é maior ou igual ao tempo de animação
    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        # Atualiza o frame do personagem andando
        indexFrameWalk = (indexFrameWalk + 1) % len(listFramesWalk)
        tempoAnimacaoWalk = 0.0

    # Atualiza a animação do personagem pulando
    tempoAnimacaoJump += dt

    # Verifica se o tempo de animação do personagem pulando é maior ou igual ao tempo de animação
    if tempoAnimacaoJump >= 1 / velocidadeAnimacaoJump:
        # Atualiza o frame do personagem pulando
        indexFrameJump = (indexFrameJump + 1) % len(listFramesJump)
        tempoAnimacaoJump = 0.0

    # Atualiza a animação do personagem correndo
    tempoAnimacaoRunn += dt

    # Verifica se o tempo de animação do personagem correndo é maior ou igual ao tempo de animação
    if tempoAnimacaoRunn >= 1 / velocidadeAnimacaoRunn:
        # Atualiza o frame do personagem correndo
        indexFrameRunn = (indexFrameRunn + 1) % len(listFramesRunn)
        tempoAnimacaoRunn = 0.0

      
       
    # Atualiza a animação do personagem morto
    tempoAnimacaoDead += dt

    #Verifica se o tempo de animação do personagem morto é maior ou igual o tempo de animação
    if tempoAnimacaoDead >= 1 /velocidadeAnimacaoDead:
        #Atualizada o framde do personagem morto
        indexFrameDead = (indexFrameDead + 1) % len(listFramesDead)
        tempoAnimacaoDead = 0.0

    # Verifica se o personagem está andando
    estaAndando = False

    # Pega as teclas que foram pressionadas
    listTeclas = pygame.key.get_pressed()


    if not GameOver:
        if listTeclas[pygame.K_LEFT]: # Verifica se a tecla esquerda foi pressionada
            direcaoPersonagem = -1 # Define a direção do personagem para a esquerda
            estaAndando = True # Define que o personagem está andando

        if listTeclas[pygame.K_RIGHT]:
            direcaoPersonagem = 1
            estaAndando = True

        if listTeclas[pygame.K_UP]: # Verifica se a tecla espaço foi pressionada
            if personagemRect.centery == ALTURA_CHAO: # Verifica se o personagem está no chão
                gravidade = -30 # Define como negativo para o personagem subir
                indexFrameJump = 0 # Reseta o frame do pulo
    else:
        if listTeclas[pygame.K_RETURN]:
            vidas = 3
            GameOver = False
            tempoJogo = 0
            velocidadePersonagem = 30
            tempoMaximoaEntreObstaculos = 3000
            listaObstaculos = []

    # Gravidade Aumenta
    gravidade += 2

    # Atualiza a posição Y do personagem de acordo com a gravidade
    personagemRect.y += gravidade

    # Verifica se o personagem está no chão
    if personagemRect.centery >= ALTURA_CHAO:
        personagemRect.centery = ALTURA_CHAO
        
    personagemColisaoRect.midbottom = personagemRect.midbottom

    # Desenha o personagem
    if not GameOver:
        if gravidade < 0: # Verifica se o personagem está subindo
            frame = listFramesJump[indexFrameJump]
        else:
            if estaAndando: # Verifica se o personagem está andando
                if velocidadePersonagem < 40:
                    frame = listFramesWalk[indexFrameWalk]
                if velocidadePersonagem < 50:
                    frame = listFramesRunn[indexFrameRunn]
                elif velocidadePersonagem < 70:
                    velocidadeAnimacaoRunn = 30
                    frame = listFramesRunn[indexFrameRunn]
                else:
                    velocidadeAnimacaoRunn = 40
                    frame = listFramesRunn[indexFrameRunn]
                
            else: # Caso contrário, o personagem está parado
                frame = listFramesIdle[indexFrameIdle]
    else:
        frame = listFramesDead[indexFrameDead]


    if direcaoPersonagem == -1: # Verifica se o personagem está olhando para a esquerda e inverte a imagem
        frame = pygame.transform.flip(frame, True, False) # Inverte a imagem

    tela.blit(frame, personagemRect) # Desenha o personagem na tela

    pygame.display.update() # Atualiza a tela

    dt = relogio.tick(60) / 1000 # Define o tempo de cada frame em segundos