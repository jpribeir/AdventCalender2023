# Day 23 of the 2023 Advent of Code
def checkNeighbours(x,y,visited_list):
    neighbour_list = []
    for (i,j) in list(counter_dir_dict.keys()):
        if x+i in range(0,len(map_matrix)) and y+j in range(0,len(map_matrix[0])):
            #if map_matrix[x+i][y+j] != "#" and map_matrix[x+i][y+j] != counter_dir_dict[(i,j)]:
            if map_matrix[x+i][y+j] != "#":
                if (x+i,y+j) not in visited_list: neighbour_list.append((x+i,y+j))
    return neighbour_list

def goThroughMap(x,y,cost,visited_list):
    neighbour_list = checkNeighbours(x,y,visited_list)
    prevX,prevY = x,y
    # While there's only 1 way possible
    while len(neighbour_list) == 1:
        (x,y) = neighbour_list[0]
        cost += 1
        neighbour_list = checkNeighbours(x,y,visited_list+[(prevX,prevY)])
        prevX,prevY = x,y
    # If not a dead-end
    if neighbour_list:
        for (i,j) in neighbour_list: goThroughMap(i,j,cost+1,visited_list+[(prevX,prevY)])
    elif x == endX and y == endY:
        global max_cost
        #max_cost = max(max_cost,cost)
        if cost > max_cost:
            print("New max",cost)
            max_cost = cost

# Read input file
with open("../include/input23.inc","r") as map_file:
    map_matrix = map_file.read().split("\n")
startX,startY = 0,map_matrix[0].index(".")
endX,endY = len(map_matrix)-1,map_matrix[-1].index(".")

########################### Part 1 ###########################
counter_dir_dict = {(-1,0): "v", (0,1): "<", (1,0): "^", (0,-1): ">",}
#print("Part 1: %s"%goThroughMap(startX,startY,0,[(startX,startY)]))

########################### Part 2 ###########################
max_cost = 0
#print("Part 2: %s"%goThroughMap(startX,startY,0,[(startX,startY)]))
goThroughMap(startX,startY,0,[(startX,startY)])
print("Part 2: %s"%max_cost)