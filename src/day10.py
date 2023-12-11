# Day 10 of the 2023 Advent of Code
def getExits(symbol):
    if symbol == "|": return [(-1,0),(1,0)]
    elif symbol == "-": return [(0,-1),(0,1)]
    elif symbol == "L": return [(-1,0),(0,1)]
    elif symbol == "J": return [(-1,0),(0,-1)]
    elif symbol == "7": return [(1,0),(0,-1)]
    elif symbol == "F": return [(1,0),(0,1)]
    else: return []

def startMaze():
    for i,line in enumerate(pipe_matrix):
        if "S" in line:
            j = line.index("S")
            copy_matrix[i] = copy_matrix[i][0:j]+"O"+copy_matrix[i][j+1:]
            neighboor_list = []
            if i>0: neighboor_list.append((-1,0))
            if i<len(pipe_matrix)-1: neighboor_list.append((1,0))
            if j>0: neighboor_list.append((0,-1))
            if j<len(pipe_matrix[0])-1: neighboor_list.append((0,1))
            for x,y in neighboor_list:
                if (x,y) in getExits(pipe_matrix[i+x][j+y]):
                    step_count = 1
                    while(pipe_matrix[i+x][j+y] != "S"):
                        copy_matrix[i+x] = copy_matrix[i+x][0:j+y]+"O"+copy_matrix[i+x][j+y+1:]
                        prevI,prevJ = i,j
                        i,j = i+x,j+y
                        step_count += 1
                        for x,y in getExits(pipe_matrix[i][j]):
                            if i+x != prevI or j+y != prevJ: break
                    return int(step_count/2)

def identifyPipeSectio():
    

# Read input file
with open("../include/input10.inc","r") as pipe_file:
    pipe_matrix = [line.strip() for line in pipe_file.readlines()]

########################### Part 1 ###########################
copy_matrix = pipe_matrix.copy()
print("Part1: %s"%startMaze())

########################### Part 2 ###########################
for each in copy_matrix: print(each)
enclosed_count = 0
for i,line in enumerate(copy_matrix):
    loop_j_count = 0
    for j,tile in enumerate(line):
        if tile == "O": loop_j_count += 1
        elif loop_j_count%2 != 0:
            loop_x_count = 0
            for x in range(0,i):
                if copy_matrix[x][j] == "O": loop_x_count += 1
            if loop_x_count%2 != 0: enclosed_count += 1
print("Part2: %s"%enclosed_count)