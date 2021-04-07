import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

LARGURA = 640
ALTURA = 480
X_RED = LARGURA//2
Y_RED = ALTURA//2
X_BLUE = randint(40,640)
Y_BLUE = randint(50, 430)
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('oJogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(120)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                X = X - 20
                
            if event.key == K_d:
                X = X + 20
                
            if event.key == K_w:
                Y = Y - 20
                
            if event.key == K_s:
                Y = Y + 20'''
                
        if pygame.key.get_pressed()[K_a]:
            X_RED -= 15
            
        if pygame.key.get_pressed()[K_d]:
            X_RED += 15
            
        if pygame.key.get_pressed()[K_w]:
            Y_RED -= 15
            
        if pygame.key.get_pressed()[K_s]:
            Y_RED += 15
         
        if X_RED >= LARGURA:
            X_RED = 0
        
        if X_RED < 0:
            X_RED = LARGURA
            
        if Y_RED >= ALTURA:
            Y_RED = 0
            
        if Y_RED < 0:
            Y_RED = ALTURA
            
            
            
        if pygame.key.get_pressed()[K_LEFT]:
            X_BLUE -= 15
            
        if pygame.key.get_pressed()[K_RIGHT]:
            X_BLUE += 15
            
        if pygame.key.get_pressed()[K_UP]:
            Y_BLUE -= 15
            
        if pygame.key.get_pressed()[K_DOWN]:
            Y_BLUE += 15
         
        if X_BLUE >= LARGURA:
            X_BLUE = 0
        
        if X_BLUE < 0:
            X_BLUE = LARGURA
            
        if Y_BLUE >= ALTURA:
            Y_BLUE = 0
            
        if Y_BLUE < 0:
            Y_BLUE = ALTURA
            
        ret_red = pygame.draw.circle(tela,(255,0,0),(X_RED,Y_RED),(10))
        ret_blue = pygame.draw.circle(tela,(0,0,255),(X_BLUE,Y_BLUE),(10))
        
        if ret_red.colliderect(ret_blue):
            print('PEGO')
            X_BLUE = randint(40,640)
            Y_BLUE = randint(50, 430)
        
        
        #pygame.draw.circle(tela,(0,0,120),(300,270),(80))
        #pygame.draw.line(tela,(255,255,0),(480,0),(390,600),(3))

        pygame.display.update()