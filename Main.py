import pygame
import random
import math
import os
import time
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800

BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def draw_window(win):
    win.blit(BACKGROUND, (0, 0))
    pygame.display.update()

def main():
    run = True
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    while (run):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        draw_window(win)

if __name__ == "__main__":
    main()