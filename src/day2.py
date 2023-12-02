# Day 2 of the 2023 Advent of Code
import re

# Read input file
with open("../include/input2.inc","r") as games_file:
    games_list = list(map(lambda a: a.strip(),games_file.readlines()))

########################### Part 1 ###########################
ball_limit_dict = {"red":12,"green":13,"blue":14}
ID_sum = 0
for game in games_list:
    set_list = re.split(": |, |; ",game)
    for set in set_list[1:]:
        if int(set.split()[0]) > ball_limit_dict[set.split()[1]]: break
    else: ID_sum += int(set_list[0].split()[1])
print("Part1: %s"%ID_sum)

########################### Part 2 ###########################
power_sum = 0
for game in games_list:
    color_min_dict = {"red":0,"green":0,"blue":0}
    set_list = re.split(": |, |; ",game)
    for set in set_list[1:]:
        color_min_dict[set.split()[1]] = max(color_min_dict[set.split()[1]],int(set.split()[0]))
    power_min = 1
    for each in color_min_dict: power_min *= color_min_dict[each]
    power_sum += power_min
print("Part1: %s"%power_sum)