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
    
