from helpers.inputs import parse_map_size
from world.world import World

if __name__ == "__main__":
    map_size = parse_map_size(input())
    world = World(*map_size)
