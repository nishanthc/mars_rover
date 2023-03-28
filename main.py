from helpers.inputs import parse_map_size, parse_initial_position_and_commands
from world.world import World

if __name__ == "__main__":
    map_size = parse_map_size(input())
    world = World(*map_size)
    initial_state_and_commands = parse_initial_position_and_commands(input())
    print(initial_state_and_commands)
