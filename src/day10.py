# Day 10 of the 2023 Advent of Code
def findSymbol(start_exit_list):
    for each in pipe_dict:
        if pipe_dict[each] == start_exit_list: return each

def replaceLine(i,j,x):
    return copy_matrix[i][0:j]+x+copy_matrix[i][j+1:]

def searchNeighbours(i,j):
    neighboor_list = []
    if i>0: neighboor_list.append((-1,0))
    if i<len(pipe_matrix)-1: neighboor_list.append((1,0))
    if j>0: neighboor_list.append((0,-1))
    if j<len(pipe_matrix[0])-1: neighboor_list.append((0,1))
    start_exit_list = []
    # In possible neighbours check if their pipe can come from present tile
    for x,y in neighboor_list:
        if (-x,-y) in pipe_dict[pipe_matrix[i+x][j+y]]: start_exit_list.append((x,y))
    return start_exit_list

def startMaze():
    for i,line in enumerate(pipe_matrix):
        if "S" in line:
            j = line.index("S")
            startI,startJ = i,j
            # Check where to go from start point and replace with appropriate symbol
            start_exit_list = searchNeighbours(i,j)
            copy_matrix[i] = replaceLine(i,j,"*")
            pipe_matrix[i] = replaceLine(i,j,findSymbol(start_exit_list))
            (x,y) = start_exit_list[0]
            step_count = 1
            # Count steps before returning to first start tile
            while not(i+x == startI and j+y == startJ):
                # Mark loop tiles in copy_matrix for 2nd part
                copy_matrix[i+x] = replaceLine(i+x,j+y,"*")
                prevI,prevJ = i,j
                i,j = i+x,j+y
                step_count += 1
                # Check possible exit tiles and pick unvisited one
                for x,y in pipe_dict[pipe_matrix[i][j]]:
                    if i+x != prevI or j+y != prevJ: break
            return int(step_count/2)

def identifyPipeSection(line):
    fromUp = False
    fromDown = False
    tile_count = 0
    while tile_count < len(line):
        if line[tile_count] == "|": return tile_count,1
        elif line[tile_count] == "L": fromUp = True
        elif line[tile_count] == "F": fromDown = True
        elif line[tile_count] == "7":
            if fromUp: return tile_count,1
            elif fromDown: return tile_count,2
        elif line[tile_count] == "J":
            if fromUp: return tile_count,2
            elif fromDown: return tile_count,1
        tile_count += 1

def countInsideTiles():
    enclosed_count = 0
    for i,line in enumerate(copy_matrix):
        loop_j_count = 0
        j = 0
        while j < len(line):
            if line[j] == "*":
                jj,loop_jj = identifyPipeSection(pipe_matrix[i][j:])
                j += jj
                loop_j_count += loop_jj
            # If tile is between odd number of pipe walls
            elif loop_j_count%2 != 0:
                loopOver,loopUnder = False,False
                x = i-1
                while (x>=0 and not loopOver):
                    if copy_matrix[x][j] == "*": loopOver = True
                    x -= 1
                # If loop has crossed over
                if loopOver:
                    x = i+1
                    while x<len(copy_matrix[0]) and not loopUnder:
                        if copy_matrix[x][j] == "*": loopUnder = True
                        x += 1
                    # If loop has crossed under
                    if loopUnder:
                        enclosed_count += 1
                        copy_matrix[i] = replaceLine(i,j,"I")
            j += 1
    return enclosed_count

# Read input file
with open("../include/input10.inc","r") as pipe_file:
    pipe_matrix = [line.strip() for line in pipe_file.readlines()]

########################### Parts 1 and 2 ###########################
pipe_dict = {"|": [(-1,0),(1,0)], "-": [(0,-1),(0,1)], "L": [(-1,0),(0,1)], "J": [(-1,0),(0,-1)], "7": [(1,0),(0,-1)], "F": [(1,0),(0,1)], ".": []}
copy_matrix = pipe_matrix.copy()
print("Part1: %s"%startMaze())
print("Part2: %s"%countInsideTiles())