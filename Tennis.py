import pygame
import sys
pygame.init()
Width,Height = 800,600
root = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Tennis")
FPS = 60


def main():
    run = True
    clock = pygame.time.Clock()
    while run == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                run == False
                sys.exit()
                break
    pygame.quit()
    
if __name__ == "__main__":
    main()