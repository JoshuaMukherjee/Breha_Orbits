from src.draw import draw
from src.Planet import Planet, read_planets_from_file
from src.Simulation import Simulation


planets, SCALE_POS = read_planets_from_file('Breha.json')


sim = Simulation(planets, G=SCALE_POS)
sim.step(300)

draw(sim, res=(1000,700), frame_rate=100, anchor_id=0, move=False)

# PERIOD =  1263
