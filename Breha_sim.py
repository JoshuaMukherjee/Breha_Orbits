from src.draw import draw
from src.Planet import Planet
from src.Simulation import Simulation

SCALE_POS=200

pos = [i*SCALE_POS for i in (0.9700436,  -0.24308753, 0)]
vel = [i for i in (0.466203685,0.43236573, 0)]

breha = Planet(pos=pos, v=vel, name='Breha',radius=10, colour=(31, 173, 67))

sun = Planet(pos=(0,0,0), v=[-2*i for i in vel], name='Sun', radius=10, colour=(252, 223, 3))

moon = Planet(pos=[-1*i for i in pos], v=vel, name='Moon', radius=10, colour=(232, 235, 233))


sim = Simulation([sun,breha,moon], G=SCALE_POS)
sim.step(300)

draw(sim, res=(1000,700), frame_rate=100, anchor_id=1, move=False)

# PERIOD =  1263
'''
TODO

- Get state on given day
- Get year from day
- Simulate spinning Breha
- Simulate light level of sun/moon
- SImulate temperature on Breha
'''
