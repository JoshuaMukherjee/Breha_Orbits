from src.Planet import Planet

class Simulation():

    def __init__(self, planets:list[Planet], G=1, anchor_planet=None):
        self.planets = planets
        self.G = G

    def set_anchor(self,anchor_planet:Planet):
        
        pos = anchor_planet.pos
        anchor_trail = anchor_planet.trail

        for planet in self.planets:
            planet.anchor_planet = anchor_planet
            
            if len(planet.trail) > 0:
                planet.trail = [i[0] - i[1] for i in zip(planet.trail, anchor_trail)]

                
                

    
    def step(self, i=1):
        for i in range(int(i)):
            for planet in self.planets:
                planet.update_velocity(self.planets, G=self.G)
            
            for planet in self.planets:
                planet.update_position()
            
            
        