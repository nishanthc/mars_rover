from helpers.inputs import parse_map_size, parse_initial_position_and_commands
from robot.robot import Robot
from world.world import World

if __name__ == "__main__":
    print("Enter a map size (e.g : '22 22' ) :")
    map_size = parse_map_size(input())
    world = World(*map_size)
    while True:
        print("Enter robot initial position and commands (e.g : '(2, 3, E) LFRFF' ) :")
        initial_position, commands = parse_initial_position_and_commands(input())
        robot = Robot(*initial_position)
        on_map, position = robot.move(world=world, commands=commands)
        print(position, "LOST" if not on_map else "")
