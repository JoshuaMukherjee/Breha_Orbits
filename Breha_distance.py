from src.Planet import Planet, read_planets_from_file, distance_scalar
from src.Simulation import Simulation

import matplotlib.pyplot as plt

planets, SCALE_POS = read_planets_from_file('Breha.json')
for planet in planets:
    if planet.name == 'Breha':
        breha = planet
    elif planet.name == 'Moon':
        moon = planet
    elif planet.name == 'Sun':
        sun = planet


sim = Simulation(planets, G=SCALE_POS)

sun_distances = []
moon_distances = []

period = planets[0].period

for i in range(period):
        
    sun_distance = distance_scalar(breha, sun)
    moon_distance = distance_scalar(breha, moon)

    sun_distances.append(sun_distance)
    moon_distances.append(moon_distance)

    sim.step(1)

plt.plot(sun_distances)
plt.plot(moon_distances)

for i in [1,2]:
    plt.vlines(i*(period/3), ymin=0, ymax=1000)

plt.show()


    