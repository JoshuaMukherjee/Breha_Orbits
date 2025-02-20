import sys
sys.path.insert(0, '.')

from src.draw import draw
from src.Planet import Planet
from src.Simulation import Simulation

sun = Planet(pos=(0,0,0), density=7, radius=10)
earth = Planet(pos=(-200,0,0), v=(0,10,0), density=0.1)
mars = Planet(pos=(300,0,0), v=(0,-10,0), density=0.1)


sim = Simulation([sun,earth,mars])

draw(sim, res=(1000,700))