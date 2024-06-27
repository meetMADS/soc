import pygame
from pygame.locals import *


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y,color_array):
        super(Square, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill(tuple(color_array))
        # self.rect = self.surf.get_rect()
        self.pos = [x, y]

    
class Rectangle(pygame.sprite.Sprite):
    def __init__(self,l,b,x_o,y_o) -> None:
        super(Rectangle,self).__init__()
        self.surf = pygame.Surface((l,b))
        self.surf.fill((128,128,128))
        self.pos= [x_o,y_o]


pygame.init()

screen = pygame.display.set_mode((800, 600))

#seeting the width of the obsatlces on a standard base of 20p
unit_measure = 20

obstacle1_in = [2,10,5,10]
obstacle2_in = [2.5,7.5,23,7.5]
obstacle3_in = [9.5,2.5,25.5,7.5]
obstacle4_in = [17.5,2.5,13,24.5]
obstacle5_in = [2.5,7,30.5,20]

obstacle_array = (obstacle1_in,obstacle2_in,obstacle3_in,obstacle4_in,obstacle5_in)
multiplied_array = [[element * 20 for element in row] for row in obstacle_array]


obstacle1=Rectangle(*(a*unit_measure for a in obstacle1_in))
obstacle2=Rectangle(*(a*unit_measure for a in obstacle2_in))
obstacle3=Rectangle(*(a*unit_measure for a in obstacle3_in))
obstacle4=Rectangle(*(a*unit_measure for a in obstacle4_in))
obstacle5=Rectangle(*(a*unit_measure for a in obstacle5_in))

obstacle_major = [obstacle1,obstacle2,obstacle3,obstacle4,obstacle5]
head_color = (0,200,250)
head = Square(40, 40,head_color)

# Use blit to put something on the screen
for object in obstacle_major:
    screen.blit(object.surf , tuple(object.pos))
screen.blit(head.surf, tuple(head.pos))

# Update the display using flip
pygame.display.flip()

direction = 'right'

main_timer = True
while main_timer:
    

    head.surf.fill((0, 0, 0))
    screen.blit(head.surf, tuple(head.pos)) # Remove old square
    head.surf.fill((0, 200, 255))
    
    pygame.time.Clock().tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            main_timer = False
    keys = pygame.key.get_pressed()

    gameOn = True
    # Our game loop
    while gameOn:
        # for loop through the event queue
        pygame.time.Clock().tick(40)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameOn = False
        keys = pygame.key.get_pressed()


        #defining the boundaries
        if head.pos[0]<=0 or head.pos[0] >=780 or head.pos[1] <=0 or head.pos[1]>= 580:
            main_timer = False
            break     
        #defining the obstacles
        for (x,y,w,z) in (multiplied_array):
            if head.pos[0]>=(w-20) and head.pos[0]<=(x+w) and head.pos[1]>=(z-20) and head.pos[1]<=(y+z):
                main_timer = False
                break

        if keys[K_w] or keys[K_UP] and direction == 'down':
            break

        if keys[K_w] or keys[K_UP]:
            direction = 'up'
            break

        if keys[K_a] or keys[K_LEFT] and direction == 'right':
            break

        if keys[K_a] or keys[K_LEFT]:
            direction = 'left'
            break

        if keys[K_s] or keys[K_DOWN] and direction == 'up':
            break

        if keys[K_s] or keys[K_DOWN]:
            direction = 'down'
            break

        if keys[K_d] or keys[K_RIGHT] and direction == 'left':
            break

        if keys[K_d] or keys[K_RIGHT]:
            direction = 'right'
            break

        else:
            direction=direction
            break
    
    if direction == 'right':
        head.pos[0] += 10
    if direction == 'left':
        head.pos[0] -= 10
    if direction == 'up':
        head.pos[1] -= 10
    if direction == 'down':
        head.pos[1] += 10

    screen.blit(head.surf, tuple(head.pos)) # Put new square
    # Update the display using flip
    pygame.display.flip()
    
pygame.quit()
