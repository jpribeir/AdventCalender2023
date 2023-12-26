# Day 23 of the 2023 Advent of Code
def checkNeighbours(x,y,visited_list):
    neighbour_list = []
    for (i,j) in [(-1,0),(0,1),(1,0),(0,-1)]:
        if x+i in range(0,len(map_matrix)) and y+j in range(0,len(map_matrix[0])):
            if map_matrix[x+i][y+j] != "#" and map_matrix[x+i][y+j] != counter_dir_dict[(i,j)]:
                if (x+i,y+j) not in visited_list: neighbour_list.append((x+i,y+j))
    return neighbour_list

def goThroughMap(x,y,cost,visited_list):
    neighbour_list = checkNeighbours(x,y,visited_list)
    # While there's only 1 way possible
    while len(neighbour_list) == 1:
        (x,y) = neighbour_list[0]
        visited_list.append((x,y))
        cost += 1
        if x == endX and y == endY: return cost
        neighbour_list = checkNeighbours(x,y,visited_list)
    # If not a dead-end
    if neighbour_list:
        cost_list = []
        for (i,j) in neighbour_list: cost_list.append(goThroughMap(i,j,cost+1,visited_list+[(i,j)]))
        return max(cost_list)
    else: return 0

# Read input file
with open("../include/example23.inc","r") as map_file:
    map_matrix = map_file.read().split("\n")
startX,startY = 0,map_matrix[0].index(".")
endX,endY = len(map_matrix)-1,map_matrix[-1].index(".")
counter_dir_dict = {(-1,0): "v", (0,1): "<", (1,0): "^", (0,-1): ">",}

########################### Part 1 ###########################
print("Part 1: %s"%goThroughMap(startX,startY,0,[(startX,startY)]))