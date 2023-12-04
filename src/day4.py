# Day 4 of the 2023 Advent of Code
def howManyMatches(line):
    numbers_list = line.split(": ")[1]
    win_list = (numbers_list.split(" | ")[0]).split()
    try_list = (numbers_list.split(" | ")[1]).split()
    match_count = 0
    for each in try_list:
        if each in win_list: match_count += 1
    return match_count

# Read input file
with open("../include/input4.inc","r") as cards_file:
    cards_list = list(map(lambda a: a.strip(),cards_file.readlines()))

########################### Part 1 ###########################
points_sum = 0
for line in cards_list:
    match_count = howManyMatches(line)
    if match_count != 0: points_sum += 2**(match_count-1)
print("Part1: %s"%points_sum)

########################### Part 2 ###########################
cards_count_list = [1]*len(cards_list)
for i,line in enumerate(cards_list):
    match_count = howManyMatches(line)
    for j in range(i+1,i+match_count+1): cards_count_list[j] += cards_count_list[i]
print("Part2: %s"%sum(cards_count_list))