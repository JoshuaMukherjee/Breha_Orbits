from src.Planet import Planet, distance_vect,distance_scalar

earth = Planet(pos=(0,0,0))
mars = Planet(pos=(0,1,5))

print(distance_vect(earth, mars))
print(distance_scalar(earth, mars))