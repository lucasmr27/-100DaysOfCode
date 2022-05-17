import random
import art
from data import data

option_a = random.randint(0, len(data) - 1)
print(art.logo)
print(f'Compare A: {data[option_a]["name"]}, {data[option_a]["description"]}, from {data[option_a]["country"]}.')
print(art.vs)
option_b = random.randint(0, len(data)-1)
print(f'Against B: {data[option_b]["name"]}, {data[option_b]["description"]}, from {data[option_b]["country"]}.')
