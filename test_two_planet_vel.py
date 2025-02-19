from src.draw import draw
from src.Planet import Planet
from src.Simulation import Simulation

earth = Planet(pos=(-200,0,0), v=(0,1,0))
mars = Planet(pos=(200,0,0), v=(0,-1,0))


sim = Simulation([earth,mars])

draw(sim)