# Day 9 of the 2023 Advent of Code
def findDifferentials(num_list):
    diff_list = []
    for i in range(1,len(num_list)): diff_list.append(num_list[i]-num_list[i-1])
    if len(set(diff_list)) > 1: return num_list[-1] + findDifferentials(diff_list)
    else: return num_list[-1] + diff_list[-1]

# Read input file
with open("../include/input9.inc","r") as sequence_file:
    sequence_list = []
    for line in sequence_file.readlines(): sequence_list.append((line.strip()).split(" "))

########################### Part 1 ###########################
extrapolate_sum = 0
for seq in sequence_list: extrapolate_sum += findDifferentials(list(map(int,seq)))
print("Part1: %s"%extrapolate_sum)

########################### Part 2 ###########################
extrapolate_sum = 0
for seq in sequence_list: extrapolate_sum -= findDifferentials(list(map(lambda x: -int(x),seq[::-1])))
print("Part2: %s"%extrapolate_sum)