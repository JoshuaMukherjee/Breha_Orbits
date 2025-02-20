import pygame
import sys
import time
from src.Planet import Planet
from src.Simulation import Simulation

class Screen:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        pygame.init()
        self.create_screen()
        self.font = pygame.font.SysFont("monospace", 15)
        self.font_large = pygame.font.SysFont("monospace", 20)

        self.half_width = int(self.width/2)
        self.half_height = int(self.height/2)


    def create_screen(self):
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Planets!!')

    def fill(self):
        self.screen.fill((0,0,0))

    def flip(self):
        pygame.display.flip()

    def draw_sprite(self,sprite):
        sprite.draw(self.screen)

    def get_height(self):
        return self.height
    
    def draw_planet(self,planet:Planet, offset_x=0, offset_y=0):

        centre = planet.get_position_2D()
        centre[0] += self.half_width
        centre[1] += self.half_height

        centre[0] -= offset_x
        centre[1] -= offset_y

        pygame.draw.circle(self.screen, color=planet.colour,center=centre,radius=planet.radius)
    
    def draw_planet_trail(self,planet:Planet, size=1, offset_x=0, offset_y=0):
        for p in planet.trail:
            pos = p[0:2].copy()

            pos[0] += self.half_width
            pos[1] += self.half_height

            pygame.draw.circle(self.screen, color=planet.colour,center=pos,radius=size)


def draw(sim:Simulation, res=(500,500), frame_rate = 20, draw_trail = True, anchor_id=None, move = True):
        screen = Screen(*res)

        n = 0

        if anchor_id is not None:
            sim.set_anchor(sim.planets[anchor_id])

        frame_1 = True
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()

            if move or frame_1:

                if anchor_id is not None:
                    anchor_planet = sim.planets[anchor_id]
                    anchor_x = anchor_planet.pos[0]
                    anchor_y = anchor_planet.pos[1]
                else:
                    anchor_x = 0
                    anchor_y = 0
                

              
                
                screen.fill()
                
                sim.step(i=1)
                
                for planet in sim.planets:
                    

                    if draw_trail:
                        screen.draw_planet_trail(planet,1, anchor_x, anchor_y)
                for planet in sim.planets:
                    screen.draw_planet(planet, anchor_x, anchor_y)

                screen.flip()
                n+= 1                
                time.sleep(1/frame_rate)

                frame_1 = False
        

            