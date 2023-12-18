# Day 18 of the 2023 Advent of Code
def newPoint(prev,dir,dist):
    if dir == "U": return [prev[0]-dist,prev[1]]
    elif dir == "D": return [prev[0]+dist,prev[1]]
    elif dir == "L": return [prev[0],prev[1]-dist]
    elif dir == "R": return [prev[0],prev[1]+dist]

def expandMap(x,y,prev_map):
    dig_map = prev_map.copy()
    if x < 0:
        for i in range(abs(x)): dig_map = [["."]*len(dig_map[0])] + dig_map
    elif x > 0:
        for i in range(abs(x)): dig_map = dig_map + [["."]*len(dig_map[0])]
    elif y < 0:
        for i in range(len(dig_map)): dig_map[i] = (["."]*abs(y)) + dig_map[i]
    elif y > 0:
        for i in range(len(dig_map)): dig_map[i] = dig_map[i] + (["."]*abs(y))
    return dig_map

def identifySection(map,x,y):
    fromUp = False
    fromDown = False
    if x>0 and dig_map[x-1][y] == "#": fromUp = True
    if x<len(dig_map)-1 and dig_map[x+1][y] == "#": fromDown = True
    if fromUp:
        if not fromDown:
            yy = 0
            while yy < len(line)-y-1 and dig_map[x][y+yy+1] == "#": yy += 1
            if x < len(dig_map)-1 and dig_map[x+1][y+yy] == "#": return 1,1+yy,yy
            else: return 0,1+yy,yy
        else: return 1,1,0
    elif fromDown:
        yy = 0
        while yy < len(line)-y-1 and dig_map[x][y+yy+1] == "#": yy += 1
        if x > 0 and dig_map[x-1][y+yy] == "#": return 1,1+yy,yy
        else: return 0,1+yy,yy

def checkOverUnder(map,x,y):
    for i in range(0,x):
        if map[i][y] == "#":
            for i in range(x+1,len(map)):
                if dig_map[i][y] == "#": return True
            else: return False

def fillMap(dig_map):
    filled_map = dig_map.copy()
    dig_count = 0
    for x,line in enumerate(dig_map):
        y = 0
        trench_count = 0
        while y < len(line):
            if dig_map[x][y] == "#":
                a,b,c = identifySection(dig_map,x,y)
                trench_count += a
                dig_count += b
                y += c
            elif trench_count%2 != 0:
                if checkOverUnder:
                    dig_count += 1
                    filled_map[x][y] = "#"
            y += 1
    return filled_map,dig_count

# Read input file
with open("../include/input18.inc","r") as dig_file:
    dig_list = list(map(lambda a: a.strip(), dig_file.readlines()))

########################### Part 1 ###########################
dig_map = [["#"]]
dig_point = [0,0]
for line in dig_list:
    extraX,extraY = 0,0
    new_point = newPoint(dig_point,line.split()[0],int(line.split()[1]))
    if new_point[0] < 0:
        extraX = new_point[0]
        new_point[0] = 0
        dig_point[0] -= extraX
    elif new_point[0] >= len(dig_map): extraX = new_point[0] - len(dig_map) + 1
    elif new_point[1] < 0:
        extraY = new_point[1]
        new_point[1] = 0
        dig_point[1] -= extraY
    elif new_point[1] >= len(dig_map[0]): extraY = new_point[1] - len(dig_map[0]) + 1
    dig_map = expandMap(extraX,extraY,dig_map)
    xrange = range(min(dig_point[0],new_point[0]),max(dig_point[0],new_point[0])+1)
    yrange = range(min(dig_point[1],new_point[1]),max(dig_point[1],new_point[1])+1)
    for x in xrange:
        for y in yrange: dig_map[x][y] = "#"
    dig_point = new_point
for line in dig_map: print("".join(line))
print("\n")
filled_map,dig_count = fillMap(dig_map)
for line in filled_map: print("".join(line))
print("Part 1: %s"%dig_count)