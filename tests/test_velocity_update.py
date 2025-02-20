import sys
sys.path.insert(0, '.')

from src.Planet import Planet, distance_vect,distance_scalar

earth = Planet(pos=(0,0,0))
mars = Planet(pos=(0,1,5))

print(earth)
earth.update_velocity([mars,])
print(earth)