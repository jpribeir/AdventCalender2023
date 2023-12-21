# Day 17 of the 2023 Advent of Code
def addDestination(x,y,dirX,dirY,dist,cost):
    # Move to new space
    x += dirX
    y += dirY
    # Check map limits
    if x in range(0,len(heat_map)) and y in range(0,len(heat_map[0])):
        cost += int(heat_map[x][y])
        # Space was not visited and it to the visited dict and add to the corresponding new cost
        if (x,y,dirX,dirY,dist) not in visited_dict:
            visited_dict[(x,y,dirX,dirY,dist)] = cost
            destination_dict.setdefault(cost,[]).append((x,y,dirX,dirY,dist))

# Read input file
with open("../include/input17.inc","r") as heat_file:
    heat_map = list(map(lambda a: a.strip(), heat_file.readlines()))

########################### Part 1 ###########################
destination_dict = {}
visited_dict = {}
# First moves are right and down from top left corner
addDestination(0,0,0,1,1,0)
addDestination(0,0,1,0,1,0)
reachedExit = False
while not reachedExit:
    # Pick existing min cost to search path, and go through possible destinations
    min_cost = min(destination_dict.keys())
    destination_list = destination_dict.pop(min_cost)
    for dest in destination_list:
        # Check left and right neighbours
        addDestination(dest[0],dest[1],-dest[3],dest[2],1,min_cost)
        addDestination(dest[0],dest[1],dest[3],-dest[2],1,min_cost)
        # And check front neighbour if max 3 in line
        if dest[4] < 3: addDestination(dest[0],dest[1],dest[2],dest[3],dest[4]+1,min_cost)
    # Check if exit was already visited (first visit should be the lowest cost visit)
    for each in visited_dict.keys():
        if each[0] == len(heat_map)-1 and each[1] == len(heat_map[0])-1:
            total_cost = visited_dict[each]
            reachedExit = True
print("Part 1: %s"%total_cost)

########################### Part 2 ###########################
destination_dict = {}
visited_dict = {}
addDestination(0,0,0,1,1,0)
addDestination(0,0,1,0,1,0)
reachedExit = False
while not reachedExit:
    min_cost = min(destination_dict.keys())
    destination_list = destination_dict.pop(min_cost)
    for dest in destination_list:
        if dest[4] >= 4:
            addDestination(dest[0],dest[1],-dest[3],dest[2],1,min_cost)
            addDestination(dest[0],dest[1],dest[3],-dest[2],1,min_cost)
        if dest[4] < 10: addDestination(dest[0],dest[1],dest[2],dest[3],dest[4]+1,min_cost)
    for each in visited_dict.keys():
        if each[0] == len(heat_map)-1 and each[1] == len(heat_map[0])-1 and each[4] >= 4:
            total_cost = visited_dict[each]
            reachedExit = True
print("Part 2: %s"%total_cost)