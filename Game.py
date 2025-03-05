import pygame
from Constants import SCREEN_WIDTH,SCREEN_HEIGHT
from Physics import Physics
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.static_objects = []
        self.dynamic_objects = []
        self.is_running = True
        self.physics = Physics()
    
    def loop(self):
        while self.is_running:
            self.screen.fill((0,0,0))
            #Render
            for object in self.static_objects:
                object.render(self.screen)
            for object in self.dynamic_objects:
                object.render(self.screen)

            for object in self.dynamic_objects:
                object.update()
                self.physics.apply_gravity(object)
                self.physics.handle_collisions(object,self.static_objects + self.dynamic_objects)
                object.move()

            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            pygame.display.update()
            pygame.time.Clock().tick(60)
            
        pygame.quit()       

    def insert_dynamic_object(self,object):
        self.dynamic_objects.append(object)

    def insert_static_object(self,object):
        self.static_objects.append(object)
