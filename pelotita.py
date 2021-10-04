import pygame, sys
from pygame.locals import *
import random
pygame.init()




def main():
    #Variables
    size = (400, 400)
    red = (255,0,0)
    r = 20
    x, y = 0+r,0+r
    vectorx, vectory = random.randint(1,3),random.randint(1,3)


    #Configs
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Pelotita")
    clock = pygame.time.Clock()


    #Bucle
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        
        window.fill((0,0,0))

        pygame.draw.circle(window, red, (x,y), r)

        if x+r > size[0] or x-r < 0:
            vectorx*=-1
        if y+r > size[1] or y-r < 0:
            vectory*=-1
        
        x+=vectorx
        y+=vectory

        pygame.display.flip()
        clock.tick(60)


    pass

if __name__ == '__main__':

    main()
