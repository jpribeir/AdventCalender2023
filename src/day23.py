# Day 23 of the 2023 Advent of Code
def checkNeighbours(x,y,prevX,prevY):
    neighbour_list = []
    dir_list = list(counter_dir_dict.keys())
    dir_list.remove((prevX-x,prevY-y))
    for (i,j) in dir_list:
        if x+i in range(0,len(map_matrix)) and y+j in range(0,len(map_matrix[0])):
            if map_matrix[x+i][y+j] != "#" and map_matrix[x+i][y+j] != counter_dir_dict[(i,j)]: neighbour_list.append((x+i,y+j))
    return neighbour_list

def checkNeighboursAndSlopes(x,y,prevX,prevY):
    neighbour_list = []
    dir_list = list(counter_dir_dict.keys())
    dir_list.remove((prevX-x,prevY-y))
    for (i,j) in dir_list:
        if x+i in range(0,len(map_matrix)) and y+j in range(0,len(map_matrix[0])):
            if map_matrix[x+i][y+j] != "#": neighbour_list.append((x+i,y+j))
    return neighbour_list

def goThroughMap(x,y,prevX,prevY,cost,visited_list):
    neighbour_list = [(x,y)]
    # While there's only 1 way possible
    while len(neighbour_list) == 1:
        (x,y) = neighbour_list[0]
        neighbour_list = checkNeighbours(x,y,prevX,prevY)
        cost += 1
        prevX,prevY = x,y
    if neighbour_list:
        if (prevX,prevY) not in visited_list:
            for (i,j) in neighbour_list: goThroughMap(i,j,prevX,prevY,cost,visited_list+[(prevX,prevY)])
    # Check if dead-end or END
    elif x == endX and y == endY:
        global max_cost
        max_cost = max(max_cost,cost-1)

def goThroughMapWithSlopes(x,y,prevX,prevY,cost,visited_list):
    neighbour_list = [(x,y)]
    # While there's only 1 way possible
    while len(neighbour_list) == 1:
        (x,y) = neighbour_list[0]
        neighbour_list = checkNeighboursAndSlopes(x,y,prevX,prevY)
        cost += 1
        prevX,prevY = x,y
    if neighbour_list:
        if (prevX,prevY) not in visited_list:
            for (i,j) in neighbour_list: goThroughMapWithSlopes(i,j,prevX,prevY,cost,visited_list+[(prevX,prevY)])
    # Check if dead-end or END
    elif x == endX and y == endY:
        global max_cost
        max_cost = max(max_cost,cost-1)

# Read input file
with open("../include/input23.inc","r") as map_file:
    map_matrix = map_file.read().split("\n")
startX,startY = 0,map_matrix[0].index(".")
endX,endY = len(map_matrix)-1,map_matrix[-1].index(".")

########################### Part 1 ###########################
counter_dir_dict = {(-1,0): "v", (0,1): "<", (1,0): "^", (0,-1): ">",}
max_cost = 0
goThroughMap(startX,startY,startX-1,startY,0,[])
print("Part 1: %s"%max_cost)

########################### Part 2 ###########################
max_cost = 0
goThroughMapWithSlopes(startX,startY,startX-1,startY,0,[])
print("Part 2: %s"%max_cost)