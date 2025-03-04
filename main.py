#import numpy as np
#import tensorflow as tf
#import gym
import pygame
pygame.init()
pygame.display.set_caption('Game test Prototype')
import random
from Constants import SCREEN_HEIGHT,SCREEN_WIDTH

from Static_Objects import Static_Rect,Static_Convex_Polygon
from Dynamic_Objects import Dynamic_Convex_Polygon
from Player import Player

from Game import Game

from utils import regular_polygon
def main():
    WALL_COLOR = (148, 93, 22)
    PLAYER_COLOR = (39, 51, 84)
    game = Game()
    player = Player( pygame.Rect((300,0,50,50)),PLAYER_COLOR)
    ground = Static_Rect( pygame.Rect((100,SCREEN_HEIGHT-400,SCREEN_WIDTH-200,10)),WALL_COLOR)
    boulder = Dynamic_Convex_Polygon( regular_polygon(8,20,(SCREEN_WIDTH - 400,430)),WALL_COLOR,(SCREEN_WIDTH - 400,430))
    slope = Static_Convex_Polygon([(0,SCREEN_HEIGHT),(SCREEN_WIDTH,SCREEN_HEIGHT),(SCREEN_WIDTH,400)],WALL_COLOR)
    game.insert_dynamic_object(player)
    #game.insert_static_object(ground)
    game.insert_dynamic_object(boulder)
    game.insert_static_object(slope)
    game.loop()
    

if __name__ == "__main__":
    main()
