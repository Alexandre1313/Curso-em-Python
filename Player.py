import pygame
import os


def main():
    pygame.init()
    tela = pygame.display.set_mode([500, 150])
    pygame.display.set_caption('ALEXX MUSIC PLAYER')
    relogio = pygame.time.Clock()
    sair = False
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                sair = True
        relogio.tick(27)
        pygame.display.update()
    pygame.quit()


main()
