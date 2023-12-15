# Day 14 of the 2023 Advent of Code
def transposeMap(input_map):
    output_map = [""]*len(input_map[0])
    for i in range(len(input_map[0])):
        for j in range(len(input_map)): output_map[i]=output_map[i]+input_map[j][i]
    return output_map

def invertLines(input_map):
    output_map = []
    for line in input_map: output_map.append(line[::-1])
    return output_map

def tiltMap(input_map):
    output_map = [""]*len(input_map)
    for i,line in enumerate(input_map):
        for part in line.split("#"):
            rock_count = part.count("O")
            output_map[i] = output_map[i]+("O"*rock_count)+("."*(len(part)-rock_count))+"#"
        output_map[i] = output_map[i][:-1]
    return output_map

def rotateMap(input_map):
    auxA_map = transposeMap(tiltMap(transposeMap(input_map)))
    auxB_map = tiltMap(auxA_map)
    auxC_map = transposeMap(invertLines(tiltMap(invertLines(transposeMap(auxB_map)))))
    return invertLines(tiltMap(invertLines(auxC_map)))

def calculateLoad(input_map):
    load_sum = 0
    for line in transposeMap(input_map):
        for j,rock in enumerate(line):
            if rock == "O": load_sum += len(line)-j
    return load_sum

# Read input file
with open("../include/example14.inc","r") as rock_file:
    rock_map = []
    for line in rock_file.readlines():
        rock_map.append(list(line.strip()))

########################### Part 1 ###########################
print("Part1: %s"%calculateLoad(transposeMap(tiltMap(transposeMap(rock_map)))))

########################### Part 2 ###########################
rotated_map = rock_map.copy()
loop_list = []
patternFound = False
count = 0
while not patternFound:
    count += 1
    if count== 20: patternFound = True 
    new_map = rotateMap(rotated_map)
    rotated_map = new_map.copy()
    new_val = calculateLoad(rotated_map)
    print(new_val)
    if new_val in loop_list:
        patternFound = True
        start = loop_list.index(new_val)
    else: loop_list.append(new_val)
total_load = loop_list[(1000000000 - start + 1)%(len(loop_list[start:]))]
print("Part2: %s"%total_load)
#for i,_ in enumerate(rotated_map): print("%s\t%s"%("".join(rock_map[i]),rotated_map[i]))