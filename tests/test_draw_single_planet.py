import sys
sys.path.insert(0, '.')

from src.draw import draw
from src.Planet import Planet
from src.Simulation import Simulation

earth = Planet()


sim = Simulation([earth,])

draw(sim, frame_rate=20)