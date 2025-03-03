#import numpy as np
#import tensorflow as tf
#import gym
import pygame
pygame.init()
pygame.display.set_caption('Game test Prototype')

from Constants import SCREEN_HEIGHT,SCREEN_WIDTH

from Static_Objects import *

from Player import *

from Game import *

def main():
    WALL_COLOR = (148, 93, 22)
    PLAYER_COLOR = (39, 51, 84)
    game = Game()
    player = Player( pygame.Rect((300,0,50,50)),PLAYER_COLOR)
    ground = Static_Rect( pygame.Rect((100,SCREEN_HEIGHT-200,SCREEN_WIDTH-200,10)),WALL_COLOR)
    pent = Static_Convex_Polygon([
        (910, 100),   # Top center point
        (310, 800),   # Bottom left point
        (910, 950),   # Bottom center point
        (1510, 800),  # Bottom right point
        (1510, 300)   # Upper right point
    ],WALL_COLOR)
    #wall1 = Static_Rect( pygame.Rect((200,0,15,SCREEN_HEIGHT)),WALL_COLOR)
    slope = Static_Convex_Polygon([(0,SCREEN_HEIGHT),(SCREEN_WIDTH,SCREEN_HEIGHT),(SCREEN_WIDTH,300)],WALL_COLOR)
    game.insert_moving_object(player)
    game.insert_static_object(ground)
    game.insert_static_object(pent)
    game.insert_static_object(slope)
    game.loop()
    

if __name__ == "__main__":
    main()
