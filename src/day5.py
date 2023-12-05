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

def getNewRanges(seed_range_list,conversion_dict):
    new_list = []
    rest_list = []
    for key in conversion_dict:
        for seed in seed_range_list:
            if seed[0]<key[0]:
                if seed[1]<key[0]:
                    rest_list.append(seed)
                elif seed[1]<=key[1]:
                    new_list.append((conversion_dict[key],conversion_dict[key]+seed[1]-key[0]))
                    rest_list.append((seed[0],key[0]))
                elif seed[1]>key[1]:
                    new_list.append((conversion_dict[key],conversion_dict[key]+key[1]-key[0]))
                    rest_list.append((seed[0],key[0]))
                    rest_list.append((key[1],seed[1]))
            elif seed[0]>=key[0]:
                if seed[0]>key[1]:
                    rest_list.append(seed)
                elif seed[1]>key[1]:
                    new_list.append((conversion_dict[key]+seed[0]-key[0],conversion_dict[key]+key[1]-key[0]))
                    rest_list.append((key[1],seed[1]))
                elif seed[1]<=key[1]:
                    new_list.append((conversion_dict[key]+seed[0]-key[0],conversion_dict[key]+seed[1]-key[0]))
        seed_range_list = list(set(rest_list.copy()))
        rest_list = []
    return new_list+seed_range_list

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
end_list = getNewNums(list(map(int,seed_list)),conversion_list)
print("Part1: %s"%min(end_list))

########################### Part 2 ###########################
seed_range_list = []
conversion_dict = {}
for line in almanac_list:
    if line.startswith("seeds:"):
        seed_list = (line.split(": ")[1]).split(" ")
        for i in range(0,len(seed_list),2): seed_range_list.append((int(seed_list[i]),int(seed_list[i])+int(seed_list[i+1])))
    elif "-to-" in line: conversion_dict = {}
    elif line == "":
        if conversion_dict: seed_range_list = getNewRanges(seed_range_list,conversion_dict)
    else: conversion_dict[(int(line.split(" ")[1]),int(line.split(" ")[1])+int(line.split(" ")[2]))] = int(line.split(" ")[0])
end_list = getNewRanges(seed_range_list,conversion_dict)
print("Part2: %s"%min(list(map(lambda a: a[0],end_list))))