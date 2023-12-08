# Day 8 of the 2023 Advent of Code
import re, math

def howManySteps(origin_node,direction,destination):
    step_count = 0
    while(not origin_node.endswith(destination)):
        origin_node = choice_dict[origin_node][0] if direction[0] == "L" else choice_dict[origin_node][1]
        direction = direction[1:]+direction[0]
        step_count += 1
    return step_count

# Read input file
choice_dict = {}
with open("../include/input8.inc","r") as map_file:
    original_direction = map_file.readline().strip()
    map_file.readline()
    for line in map_file.readlines():
        matches = re.findall("([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)",line)
        choice_dict[matches[0][0]] = (matches[0][1],matches[0][2])

########################### Part 1 ###########################
print("Part1: %s"%howManySteps("AAA",original_direction,"ZZZ"))

########################### Part 2 ###########################
steps_list = []
for node in choice_dict:
    if node.endswith("A"): steps_list.append(howManySteps(node,original_direction,"Z"))
step_count = 1
for each in steps_list: step_count = step_count*each//math.gcd(step_count,each)
print("Part2: %s"%step_count)