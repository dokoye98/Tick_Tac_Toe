import pygame
import sys
pygame.init()
Width,Height = 800,600
PaddleW,PaddleH = 15,90
ROOT = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Tennis")
FPS = 60
SCORE = pygame.font.SysFont("comicsans",40)
winning_score = 10
def colour_wheel(red,blue,yellow):
    colour = (red,blue,yellow)
    return colour


def draw(root,paddles,ball,leftsc,rightsc):
    root.fill(colour_wheel(0,0,0))
    leftsc = SCORE.render(f"{leftsc}",1,colour_wheel(255,255,255))
    rightsc = SCORE.render(f"{rightsc}",1,colour_wheel(255,255,255))
    ROOT.blit(leftsc,(Width//4- leftsc.get_width()//2,20))
    ROOT.blit(leftsc,(Width*(3/4)- rightsc.get_width()//2,20))
    for paddle in paddles:
        paddle.draw(root)
    ball.draw(root)
    
    pygame.display.update()
    
def handle_collision(ball,left,right):
    if ball.y +ball.radius >= Height:
        ball.y_vel*=-1
    elif ball.y - ball.radius <=0:
        ball.y_vel *= -1
    
    if ball.x_vel <0:
        if ball.y >=left.y and ball.y <=left.y + left.height:
            if ball.x - ball.radius <= left.x + left.width:
                ball.x_vel *= -1   
                
                middle_y = left.y + left.height /2
                diff_y =  middle_y -ball.y
                reduction = (left.height / 2)/ ball.MAX_VEL
                y_vel = diff_y /reduction  
                ball.y_vel =-1* (y_vel//10)    
    else:
        if ball.y >= right.y and ball.y <= right.y + right.height:
            if ball.x + ball.radius >= right.x:
                ball.x_vel *=-1
                middle_y = left.y + right.height /2
                diff_y =  middle_y -ball.y
                reduction = (left.height / 2)/ ball.MAX_VEL
                y_vel = diff_y /reduction  
                ball.y_vel =-1* (y_vel//10)    
class Paddle:
    COlOUR = colour_wheel(255,255,255)
    VEL = 9
    def __init__(self,x,y,width,height):
        self.x =self.orig_x= x
        self.y = self.orig_y = y
        self.width = width
        self.height = height
    def draw(self,root):
        pygame.draw.rect(ROOT,self.COlOUR,(self.x,self.y,self.width,self.height))
    
    def move(self,down=True):
        if down:
            self.y +=self.VEL
        else:
            self.y -=self.VEL

    def reset(self):
        self.y = self.orig_y
        self.x = self.orig_y

class Ball:
    MAX_VEL = 10
    color = colour_wheel(255,255,255)
    def __init__(self,x,y,radius) -> None:
        self.x = self.original_x = x 
        self.y = self.orignal_y = y
        
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
    def draw(self,root):
        pygame.draw.circle(root,self.color,(self.x,self.y),self.radius)
    
    def move(self):
        self.x +=self.x_vel
        self.y +=self.y_vel
    def reset(self):
        self.x = self.original_x - 40
        self.y = self.orignal_y 
        self.y_vel =0
        self.x_vel  *=-1
        
        
        
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
    ball = Ball(Width//2,Height//2,7)
    left_score = 0
    right_score = 0
    while run == True:
        clock.tick(60)
        draw(ROOT,[left_paddle,right_paddle],ball,left_score,right_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                sys.exit()
                
        keys = pygame.key.get_pressed()
        handle_paddle_mvove(keys,left_paddle,right_paddle)   
        ball.move()
        handle_collision(ball,left_paddle,right_paddle)
        if ball.x == 0:
            right_score +=1
            ball.reset()
        elif ball.x > Width:
            left_score +=1
            ball.reset()
            
        won = False
        if left_score >= winning_score:
            won = True
            win_Text = "Left WINS"
        if right_score >= winning_score:
            won = True
            win_Text = "Right WINS"
        if won == True:  
            TE = SCORE.render(win_Text,1,colour_wheel(255,255,255))
            ROOT.blit(TE,(Width//2-TE.get_width()//2,Height//2- TE.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            left_paddle.reset()
            right_paddle.reset()
            ball.reset()
            
if __name__ == "__main__":
    main()