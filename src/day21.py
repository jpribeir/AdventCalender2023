# Day 21 of the 2023 Advent of Code
def findStart():
    for i,_ in enumerate(garden_map):
        if "S" in garden_map[i]:
            j = garden_map[i].index("S")
            garden_map[i] = garden_map[i][0:j]+"."+garden_map[i][j+1:]
            return (i,j)

def takeStep(x,y,next_list):
    if x in range(0,len(garden_map)) and y in range(0,len(garden_map[0])):
        if garden_map[x][y] != "#":
            if (x,y) not in next_list: next_list.append((x,y))
    return next_list

def getStepsIn(num_steps,behind_list):
    for _ in range(num_steps):
        next_list = []
        for (x,y) in behind_list:
            for (dx,dy) in [(-1,0),(0,1),(1,0),(0,-1)]: next_list = takeStep(x+dx,y+dy,next_list)
        behind_list = next_list.copy()
    return(len(next_list))

# Read input file
with open("../include/input21.inc","r") as garden_file:
    garden_map = garden_file.read().split("\n")

########################### Part 1 ###########################
print("Part 1: %s"%getStepsIn(64,[findStart()]))