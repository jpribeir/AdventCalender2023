# Day 15 of the 2023 Advent of Code
def updateHash(val,current):
    return (17*(val + ord(current)))%256

def getHash(code):
    val = 0
    for char in code: val = updateHash(val,char)
    return val

def getInfo(code):
    if "=" in code:
        label = code.split("=")[0]
        lens_str = code.split("=")[1]
    elif "-" in code:
        label = code.split("-")[0]
        lens_str = None
    return label,getHash(label),lens_str

# Read input file
with open("../include/input15.inc","r") as hash_file:
    hash_list = ((hash_file.readline()).strip()).split(",")

########################### Part 1 ###########################
hash_sum = 0
for each in hash_list: hash_sum += getHash(each)
print("Part1: %s"%hash_sum)

########################### Part 2 ###########################
box_dict = {}
for each in hash_list:
    label,box,lens_str = getInfo(each)
    if "=" in each:
        if box not in box_dict.keys(): box_dict[box] = [label+" "+lens_str]
        else:
            for i,lens in enumerate(box_dict[box]):
                if label in lens:
                    (box_dict[box])[i] = label+" "+lens_str
                    break
            else: box_dict[box].append(label+" "+lens_str)
    elif "-" in each:
        if box in box_dict.keys():
            for lens in box_dict[box]:
                if label in lens:
                    (box_dict[box]).remove(lens)
                    break
            if box_dict[box] == []: del(box_dict[box])
focus_pwr = 0
for box in box_dict:
    for i,lens in enumerate(box_dict[box]): focus_pwr += (box+1)*(i+1)*(int(lens.split(" ")[1]))
print("Part2: %s"%focus_pwr)