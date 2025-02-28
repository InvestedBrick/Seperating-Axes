#import numpy as np
#import tensorflow as tf
#import gym
import pygame
pygame.init()
pygame.display.set_caption('Game test Prototype')

from Constants import SCREEN_HEIGHT,SCREEN_WIDTH

from Static_Object import *

from Player import *

from Game import *

def main():
    WALL_COLOR = (148, 93, 22)
    game = Game()
    player = Player( pygame.Rect((300,200,50,50)),(39, 51, 84))
    ground = Static_Object( pygame.Rect((100,550,SCREEN_WIDTH-200,10)),WALL_COLOR)
    wall1 = Static_Object( pygame.Rect((500,0,15,SCREEN_HEIGHT)),WALL_COLOR)
    game.insert_moving_object(player)
    game.insert_static_object(ground)
    game.insert_static_object(wall1)
    game.loop()
    

if __name__ == "__main__":
    main()
