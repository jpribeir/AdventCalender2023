# Day 3 of the 2023 Advent of Code
def checkNum(i,num_init,num_last):
    for x in range(max(num_init-1,0),min(num_last+2,max_j+1)):
        if i>0:
            if engine_list[i-1][x] != "." and not engine_list[i-1][x].isdigit(): return True
        if i<max_i:
            if engine_list[i+1][x] != "." and not engine_list[i+1][x].isdigit(): return True
    if num_init>0:
        if engine_list[i][num_init-1] != "." and not engine_list[i][num_init-1].isdigit(): return True
    if num_last<max_j:
        if engine_list[i][num_last+1] != "." and not engine_list[i][num_last+1].isdigit(): return True
    return False

# Read input file
with open("../include/input3.inc","r") as engine_file:
    engine_list = list(map(lambda a: a.strip(),engine_file.readlines()))

########################### Part 1 ###########################
max_i = len(engine_list)-1
max_j = len(engine_list[0])-1
engine_sum = 0
checkingNum = False
for i,row in enumerate(engine_list):
    for j,col in enumerate(row):
        if col.isdigit():
            if not checkingNum:
                #print(i,j)
                new_num = col
                num_init = j
                checkingNum = True
            else: new_num += col
        else:
            if checkingNum:
                checkingNum = False
                if checkNum(i,num_init,j-1): engine_sum += int(new_num)
    else:
        if checkingNum:
            checkingNum = False
            if checkNum(i,num_init,j-1): engine_sum += int(new_num)

print("Part1: %s"%engine_sum)