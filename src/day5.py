# Day 5 of the 2023 Advent of Code
def getNewNums(seed_list,conversion_list):
    new_list = []
    for seed in seed_list:
        for conv in conversion_list:
            if seed in range(conv[1],conv[1]+conv[2]):
                new_list.append(seed-conv[1]+conv[0])
                break
        else: new_list.append(seed)
    return new_list

# Read input file
with open("../include/input5.inc","r") as almanac_file:
    almanac_list = list(map(lambda a: a.strip(),almanac_file.readlines()))

########################### Part 1 ###########################
conversion_list = []
for line in almanac_list:
    if line.startswith("seeds:"): seed_list = (line.split(": ")[1]).split(" ")
    elif "-to-" in line: conversion_list = []
    elif line == "": seed_list = getNewNums(list(map(int,seed_list)),conversion_list)
    else: conversion_list.append(list(map(int,line.split(" "))))
seed_list = getNewNums(list(map(int,seed_list)),conversion_list)
print("Part1: %s"%min(seed_list))