import numpy as np
from numpy import array
import random
import json

class Planet():

    def __init__(self,pos = (0,0,0), radius = 10, density = None, v=(0.,0,0), colour = None, name=None, period=1263, anchor_planet=None):

        self.name = '' if name is None else name

        self.pos = np.asarray(pos,dtype=np.float64)

        self.v = np.asarray(v,dtype=np.float64)
        
        self.radius = radius
        self.volume = 4/3 * 3.14159 * self.radius**3
        self.density = density
        if self.density is not None:
            self.mass = self.volume * self.density
        else:
            self.mass = 1

        if colour is None:
            self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        else:
            self.colour = colour

        
        self.period = 1263
        self.trail = []

        self.anchor_planet = anchor_planet


    def __str__(self) -> str:

        return f"{self.name}, Position {self.pos}, Velocity {self.v}"

    def update_velocity(self, planets, G=1):
        for planet in planets:
            if planet != self:
                dist = distance_vect(self, planet)
                d = distance_scalar(self, planet)
                self.v += (G * planet.mass / d**3) * dist
    
    def update_position(self):
        if self.anchor_planet is not None:
            d_pos = self.anchor_planet.pos
        else:
            d_pos = 0
        
        self.trail.append(self.pos.copy() - d_pos)
        self.pos += self.v

    
    def get_position_2D(self) -> array:
        return self.pos[:2].copy()
    


def distance_vect(planet:Planet, other:Planet) -> array:
    p1 = planet.pos
    p2 = other.pos

    return p2-p1

def distance_scalar(planet:Planet, other:Planet) -> float:
    dv = distance_vect(planet, other)
    return np.sqrt(np.sum(dv**2))


def read_planets_from_file(path) -> tuple[list[Planet], int]:
    f = json.loads(open(path).read())
    pnts = f['planets']
    scale = f['scale']

    planets = []


    for name in pnts:
        data = pnts[name]
        
        pos = np.asarray(data['pos']) * scale
        vel = np.asarray(data['vel'])

        radius = data['radius'] if 'radius' in data else 10
        density = data['density'] if 'density' in data else None
        colour = data['colour'] if 'colour' in data else None
        
        planet = Planet(pos=pos,radius=radius,density=density, v=vel, colour=colour,name=name )

        planets.append(planet)

    return planets, scale