# Day 6 of the 2023 Advent of Code
# Read input file
with open("../include/input6.inc","r") as boat_race_file:
    time_list = list(map(int,((boat_race_file.readline()).split(":")[1]).split()))
    distance_list = list(map(int,((boat_race_file.readline()).split(":")[1]).split()))

########################### Part 1 ###########################
record_power = 1
for i,_ in enumerate(time_list):
    record_count = 0
    for x in range(time_list[i]):
        if (time_list[i]-x)*x > distance_list[i]: record_count += 1
    record_power *= record_count
print("Part1: %s"%record_power)

########################### Part 2 ###########################
big_time = int("".join(list(map(str,time_list))))
big_distance = int("".join(list(map(str,distance_list))))
record_count = 0
for x in range(big_time):
    if (big_time-x)*x > big_distance: record_count += 1
print("Part2: %s"%record_count)