# Day 13 of the 2023 Advent of Code

# Read input file
with open("../include/example13.inc","r") as map_file:
    map_list = []
    new_map = []
    for line in list(map(lambda a: a.strip(),map_file.readlines())):
        if not line:
            map_list.append(new_map)
            new_map = []
        else: new_map.append(line)
    map_list.append(new_map)

########################### Part 1 ###########################

print("Part1: %s"%startMaze())