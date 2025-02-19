from src.draw import draw
from src.Planet import Planet
from src.Simulation import Simulation

SCALE_POS=200

pos = [i*SCALE_POS for i in (0.9700436,  -0.24308753, 0)]
vel = [i for i in (0.466203685,0.43236573, 0)]



sun = Planet(pos=(0,0,0), v=[-2*i for i in vel])

earth = Planet(pos=pos, v=vel)

moon = Planet(pos=[-1*i for i in pos], v=vel)


sim = Simulation([sun,earth,moon], G=SCALE_POS)

draw(sim, res=(1000,700), frame_rate=100)

# PERIOD =  1263
