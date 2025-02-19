



def distance_vect(planet:Planet, other:Planet) -> array:
    p1 = planet.pos
    p2 = other.pos

    return p2-p1

def distance_scalar(planet:Planet, other:Planet) -> float:
    dv = distance_vect(planet, other)
    return np.sqrt(np.sum(dv**2))