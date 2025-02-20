import sys
sys.path.insert(0, '.')

from src.Planet import read_planets_from_file

planets, scale = read_planets_from_file('Breha.json')

print(planets)