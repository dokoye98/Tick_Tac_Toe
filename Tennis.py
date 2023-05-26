import pygame
import sys
pygame.init()
Width,Height = 800,600
PaddleW,PaddleH = 15,90
ROOT = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Tennis")
FPS = 60

def colour_wheel(red,blue,yellow):
    colour = (red,blue,yellow)
    return colour


def draw(root,paddles):
    root.fill(colour_wheel(0,0,0))
    for paddle in paddles:
        paddle.draw(root)
   
    


class Paddle:
    COlOUR = colour_wheel(255,255,255)
    VEL = 9
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,root):
        pygame.draw.rect(ROOT,self.COlOUR,(self.x,self.y,self.width,self.height))
    
    def move(self,down=True):
        if down:
            self.y +=self.VEL
        else:
            self.y -=self.VEL
        
        
def handle_paddle_mvove(keys,left,right):
    if keys[pygame.K_w] and left.y - left.VEL >=0:
        left.move(down = False)
    if keys[pygame.K_s] and left.y + left.VEL + left.height <= Height:
        left.move(down = True)
    
    if keys[pygame.K_DOWN] and right.y - right.VEL + right.height <=Height:
        right.move(down = True)
    if keys[pygame.K_UP] and right.y - right.VEL>=0:
        right.move(down = False)
    
        
def main():
    run = True
    clock = pygame.time.Clock()
    left_paddle = Paddle(10,Height//2 - PaddleH/2,PaddleW,PaddleH)
    right_paddle = Paddle(Width - 10 - PaddleW,Height//2 - PaddleH/2,PaddleW,PaddleH)
    while run == True:
        clock.tick(FPS)
        draw(ROOT,[left_paddle,right_paddle])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                sys.exit()
                
        keys = pygame.key.get_pressed()
        handle_paddle_mvove(keys,left_paddle,right_paddle)
                
    
    
if __name__ == "__main__":
    main()