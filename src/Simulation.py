from src.Planet import Planet

class Simulation():

    def __init__(self, planets:list[Planet], G=1):
        self.planets = planets
        self.G = G

    
    def step(self):
        for planet in self.planets:
            planet.update_velocity(self.planets, G=self.G)
        
        for planet in self.planets:
            planet.update_position()
        
        
        