# Day 10 of the 2023 Advent of Code
def getExits(symbol):
    if symbol == "|": return [(-1,0),(1,0)]
    elif symbol == "-": return [(0,-1),(0,1)]
    elif symbol == "L": return [(-1,0),(0,1)]
    elif symbol == "J": return [(-1,0),(0,-1)]
    elif symbol == "7": return [(1,0),(0,-1)]
    elif symbol == "F": return [(1,0),(0,1)]
    else: return []

def goThroughPipe(prevI,prevJ,newI,newJ,step_count):
    print("Step %s | %s , %s"%(step_count,newI,newJ))
    if pipe_matrix[newI][newJ] == "S": return step_count
    for x,y in getExits(pipe_matrix[newI][newJ]):
        if (newI+x,newJ+y) != (prevI,prevJ): return goThroughPipe(newI,newJ,newI+x,newJ+y,step_count+1)

def startMaze(i,j):
    neighboor_list = []
    if i>0: neighboor_list.append((-1,0))
    if i<len(pipe_matrix)-1: neighboor_list.append((1,0))
    if j>0: neighboor_list.append((0,-1))
    if j<len(pipe_matrix[0])-1: neighboor_list.append((0,1))
    for x,y in neighboor_list:
        if (x,y) in getExits(pipe_matrix[i+x][j+y]):
            step_count = 0
            prevI,prevJ = i,j
            i,j = i+x,j+y
            while(pipe_matrix[i][j] != "S"):
                step_count += 1
                print("Step %s | %s , %s"%(step_count,i,j))
                for x,y in getExits(pipe_matrix[i+x][j+y]):
                    if (i+x,j+y) != (prevI,prevJ):
                        prevI,prevJ = i,j
                        i,j = i+x,j+y
                else:
                    print("Got stuck at %x,%x"%(i,j))
                    exit()
            return int(step_count/2)

# Read input file
with open("../include/example10.inc","r") as pipe_file:
    pipe_matrix = [line.strip() for line in pipe_file.readlines()]

########################### Part 1 ###########################
for i,line in enumerate(pipe_matrix):
    if "S" in line:
        j = line.index("S")
        break
print("Part1: %s"%startMaze(i,j))