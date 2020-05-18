import random #for generating random numbers
import sys #we will use sys.exit to exit the game
import pygame
import pygame.locals import *

fps =32
screen_width = 289
screen_height = 511
screen = pygame.display.set_mode((screen_width,screen_height))
groundy = screen_height*0.8
game_sprites = {}
game_sounds = {}
player = '/galery/sprites/bird.png'
background = '/galery/sprites/background.png'
pipe = '/galery/sprites/pipe.png'

if __name__ == "__main__":
    #this will be the main point from where our game starts
    pygame.init()#initialise all pygame modules
    fpsclock = pygame.time.clock()
    pygame.display.set_caption('flappy bird')
    game_sprites['number'] = (
        pygame.image.load('/galery/sprites/0.png').convert_alpha(),
        pygame.image.load('/galery/sprites/1.png').convert_alpha(),
        pygame.image.load('/galery/sprites/2.png').convert_alpha(),
        pygame.image.load('/galery/sprites/3.png').convert_alpha(),
        pygame.image.load('/galery/sprites/4.png').convert_alpha(),
        pygame.image.load('/galery/sprites/5.png').convert_alpha(),
        pygame.image.load('/galery/sprites/6.png').convert_alpha(),
        pygame.image.load('/galery/sprites/7.png').convert_alpha(),
        pygame.image.load('/galery/sprites/8.png').convert_alpha(),
        pygame.image.load('/galery/sprites/9.png').convert_alpha(),

    )

    game_sprites['message'] = pygame.image.load('/galery/sprites/message.png').convert_alpha()
    game_sprites['base'] = pygame.image.load('/galery/sprites/message.png').convert_alpha()
    game_sprites['pipe'] = (
    
    
    pygame.transform.rotate(pygame.image.load('/galery/sprites/message.png').convert_alpha(),180),
    pygame.image.load('/galery/sprites/message.png').convert_alpha()
    
    )