# Day 17 of the 2023 Advent of Code
def addState(x,y,dirX,dirY,dist,prev_cost):
    x += dirX
    y += dirY
    dist += 1
    if x in range(0,len(heat_map)) and y in range(0,len(heat_map[0])):
        cost = prev_cost + int(heat_map[x][y])
        if (x,y,dirX,dirY,dist) not in visited_dict:
            visited_dict[(x,y,dirX,dirY,dist)] = cost
            queue_dict.setdefault(cost,[]).append((x,y,dirX,dirY,dist))

# Read input file
with open("../include/example17.inc","r") as heat_file:
    heat_map = list(map(lambda a: a.strip(), heat_file.readlines()))

########################### Part 1 ###########################
queue_dict = {}
visited_dict = {}
addState(0,0,0,1,0,0)
addState(0,0,1,0,0,0)
reachedExit = False
while not reachedExit:
    min_cost = min(queue_dict.keys())
    state_list = queue_dict.pop(min_cost)
    check_exit_list = []
    for state in state_list:
        ### NEED TO UPDATE THIS STILL TO ACCOUNT FOR DIRECTIONS AND DISTANCE ###
        addState(state[0]+1,state[1],min_cost)
        addState(state[0],state[1]+1,min_cost)
        addState(state[0]-1,state[1],min_cost)
        addState(state[0],state[1]-1,min_cost)
    if (len(heat_map)-1,len(heat_map[0])-1) in visited_dict.keys():
        total_cost = visited_dict[(len(heat_map)-1,len(heat_map[0])-1)]
        reachedExit = True
print("Part 1: %s"%total_cost)