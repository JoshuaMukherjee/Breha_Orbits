import sys
sys.path.insert(0, '.')

from src.draw import draw
from src.Planet import Planet
from src.Simulation import Simulation
import random


N = 100

MIN = -200
MAX = 200

planets = []
for i in range(N):
    pos = (random.randint(MIN,MAX),random.randint(MIN,MAX),random.randint(MIN,MAX))
    r = random.randint(1,10)
    planets.append(Planet(pos=pos,radius=r, density=1))


sim = Simulation(planets, G=1)

draw(sim, frame_rate=20, res=(700,700))