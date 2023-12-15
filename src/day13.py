# Day 13 of the 2023 Advent of Code
def verticalSweep(map):
    for i,line in enumerate(map):
        if line == map[-1]: return 100*(len(map)-round((len(map)-i)/2))
    else:
        for i,line in enumerate(map[::-1]):
            if line == map[-1]: return 100*(len(map)-round(len(map)-i))
        else: return None

def horizontalSweep(map):
    new_map = [[0*len(map)]*len(map[0])]
    for i,line in enumerate(map):
        for j,_ in enumerate(line):
            new_map[j][i] = map[i][j]
    for each in map: print(each)
    for each in new_map: print(each)
    return verticalSweep(new_map)/100

# Read input file
with open("../include/example13.inc","r") as map_file:
    map_list = []
    new_map = []
    for line in list(map(lambda a: a.strip(),map_file.readlines())):
        if not line:
            map_list.append(new_map)
            new_map = []
        else: new_map.append(list(line))
    map_list.append(new_map)
for map in map_list:
    for each in map: print(each)

########################### Part 1 ###########################
summarize_total = 0
for map in map_list:
    new_val = verticalSweep(map)
    if not new_val: new_val = horizontalSweep(map)
    summarize_total += new_val
print("Part1: %s"%summarize_total)