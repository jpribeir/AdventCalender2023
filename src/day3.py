# Day 3 of the 2023 Advent of Code
# Store cogs' coordinates, numbers adjacent and their total power
class Cog():
    def __init__(self,x,y,new_num):
        self.x = x
        self.y = y
        self.power = int(new_num)
        self.adjacent_nums = 1
    def powerIt(self,new_num):
        self.power = self.power * int(new_num)
        self.adjacent_nums += 1

def checkNum(i,num_init,num_last):
    numFound = False
    cogFound = False
    cogX,cogY = 0,0
    for x in range(max(num_init-1,0),min(num_last+2,max_j+1)):
        # If not first line, check previous line
        if i>0:
            if engine_list[i-1][x] != "." and not engine_list[i-1][x].isdigit():
                numFound = True
                if engine_list[i-1][x] == "*":
                    cogFound = True
                    cogX,cogY = i-1,x
        # If not last line, check next line
        if i<max_i:
            if engine_list[i+1][x] != "." and not engine_list[i+1][x].isdigit():
                numFound = True
                if engine_list[i+1][x] == "*":
                    cogFound = True
                    cogX,cogY = i+1,x
    # If not first collumn, check previous collumn
    if num_init>0:
        if engine_list[i][num_init-1] != "." and not engine_list[i][num_init-1].isdigit():
                numFound = True
                if engine_list[i][num_init-1] == "*":
                    cogFound = True
                    cogX,cogY = i,num_init-1
    # If not last collumn, check next collumn
    if num_last<max_j:
        if engine_list[i][num_last+1] != "." and not engine_list[i][num_last+1].isdigit():
                numFound = True
                if engine_list[i][num_last+1] == "*":
                    cogFound = True
                    cogX,cogY = i,num_last+1
    return numFound,cogFound,cogX,cogY

def updateCogDict(cogX,cogY,new_num):
    for cog in cog_dict:
        if (cogX,cogY) == cog:
            (cog_dict[(cogX,cogY)]).powerIt(new_num)
            return
    else: cog_dict[(cogX,cogY)] = Cog(cogX,cogY,new_num)

# Read input file
with open("../include/input3.inc","r") as engine_file:
    engine_list = list(map(lambda a: a.strip(),engine_file.readlines()))

########################### Parts 1 and 2 ###########################
max_i = len(engine_list)-1
max_j = len(engine_list[0])-1
cog_dict = {}
engine_sum = 0
checkingNum = False
for i,row in enumerate(engine_list):
    for j,col in enumerate(row):
        if col.isdigit():
            if not checkingNum:
                new_num = col
                num_init = j
                checkingNum = True
            else: new_num += col
        # If end of number is found
        else:
            if checkingNum:
                checkingNum = False
                numFound,cogFound,cogX,cogY = checkNum(i,num_init,j-1)
                if numFound: engine_sum += int(new_num)
                if cogFound: updateCogDict(cogX,cogY,new_num)
    # If end of number is at end of line
    else:
        if checkingNum:
            checkingNum = False
            numFound,cogFound,cogX,cogY = checkNum(i,num_init,j-1)
            if numFound: engine_sum += int(new_num)
            if cogFound: updateCogDict(cogX,cogY,new_num)
print("Part1: %s"%engine_sum)

cog_sum = 0
for cog in cog_dict:
    if cog_dict[cog].adjacent_nums == 2: cog_sum += cog_dict[cog].power
print("Part2: %s"%cog_sum)